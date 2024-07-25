import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime, timedelta

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

# Configure Flask app with MongoDB
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

# Initialize PyMongo
mongo = PyMongo(app)


# Define Schemas
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password
        }


class Definition:
    def __init__(self, term, definition, created_by=None):
        self.term = term
        self.definition = definition
        self.created_by = created_by

    def to_dict(self):
        return {
            "term": self.term,
            "definition": self.definition,
            "created_by": self.created_by,
        }


@app.before_request
def check_session():
    """Check if the session is valid; if not, log out the user."""
    if 'user' in session:
        last_active = (
            session.get('last_active', datetime.utcnow())
            .replace(tzinfo=None)
        )
        current_time = datetime.utcnow()
        session_lifetime = app.config['PERMANENT_SESSION_LIFETIME']
        if (current_time - last_active) > session_lifetime:
            session.pop('user', None)
            return redirect(url_for('index'))
        session['last_active'] = current_time


# Routes
@app.route('/')
def index():
    # Fetch all definitions sorted by term alphabetically
    all_definitions = list(mongo.db.definitions.find().sort('term', 1))
    return render_template('index.html', definitions=all_definitions)


@app.route('/browse/<letter>')
def browse(letter):
    """Fetch definitions that start with the selected letter."""
    if letter == '*':
        definitions = list(mongo.db.definitions.find({}))
    else:
        regex = f'^{letter}'
        definitions = list(
            mongo.db.definitions.find(
                {'term': {'$regex': regex, '$options': 'i'}}
            )
        )
    return render_template(
        'browse.html',
        definitions=definitions,
        letter=letter
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = mongo.db.users
        user = users.find_one({'username': username})

        if user and check_password_hash(user['password'], password):
            session['user'] = str(user['_id'])
            session['last_active'] = datetime.utcnow().replace(tzinfo=None)
            return redirect(url_for('index'))
        else:
            message = "Invalid username or password"
            return render_template('login.html', message=message)

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('last_active', None)
    return redirect(url_for('index'))


@app.route('/add_term', methods=['GET', 'POST'])
def add_term():
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        term = request.form['term'].capitalize()
        definition = request.form['definition']
        created_by = ObjectId(session['user'])

        definition_doc = Definition(
            term=term,
            definition=definition,
            created_by=created_by
        )
        mongo.db.definitions.insert_one(definition_doc.to_dict())
        return redirect(url_for('index'))

    return render_template('add_term.html')


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if query:
        matching_definitions = list(
            mongo.db.definitions.find(
                {'term': {'$regex': query, '$options': 'i'}}
            )
        )
    else:
        matching_definitions = []

    message = (
        "No results found." if not matching_definitions and query
        else None
    )
    return render_template(
        'index.html',
        definitions=matching_definitions,
        message=message
    )


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Passwords do not match!')
            return redirect(url_for('register'))

        users = mongo.db.users
        existing_user = users.find_one({'username': username})

        if existing_user is None:
            user = User(username=username, password=password)
            users.insert_one(user.to_dict())
            user_id = users.find_one({'username': username})['_id']
            session['user'] = str(user_id)
            session.permanent = True
            session['last_active'] = datetime.utcnow()
            return redirect(url_for('index'))
        else:
            flash('Username already exists!')
            return redirect(url_for('register'))

    return render_template('register.html')


@app.route('/edit_term/<term_id>', methods=['GET', 'POST'])
def edit_term(term_id):
    if 'user' not in session:
        return redirect(url_for('login'))

    term = mongo.db.definitions.find_one({'_id': ObjectId(term_id)})

    if term and term['created_by'] == ObjectId(session['user']):
        if request.method == 'POST':
            new_term = request.form['term']
            new_definition = request.form['definition']
            mongo.db.definitions.update_one(
                {'_id': ObjectId(term_id)},
                {'$set': {
                    'term': new_term,
                    'definition': new_definition
                }}
            )
            return redirect(url_for('index'))
        return render_template('edit_term.html', term=term)

    return redirect(url_for('index'))


@app.route('/delete_term/<term_id>', methods=['POST'])
def delete_term(term_id):
    if 'user' not in session:
        return redirect(url_for('login'))

    term = mongo.db.definitions.find_one({'_id': ObjectId(term_id)})

    if term and term['created_by'] == ObjectId(session['user']):
        mongo.db.definitions.delete_one({'_id': ObjectId(term_id)})
        return redirect(url_for('index'))

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP", "0.0.0.0"),
            port=int(os.environ.get("PORT", 5000)),
            debug=True)
