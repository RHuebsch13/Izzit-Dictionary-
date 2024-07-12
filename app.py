import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

# Configure Flask app with MongoDB
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# Initialize PyMongo
mongo = PyMongo(app)

# Routes
@app.route('/')
def index():
    # Fetch all definitions sorted by term alphabetically
    all_definitions = list(mongo.db.definitions.find().sort('term', 1))
    # Format dates for display
    for definition in all_definitions:
        if 'created_at' in definition:
            definition['created_at'] = definition['created_at'].strftime('%Y-%m-%d %H:%M:%S')
        if 'updated_at' in definition:
            definition['updated_at'] = definition['updated_at'].strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', definitions=all_definitions)


@app.route('/browse/<letter>')
def browse(letter):
    # Fetch definitions that start with the selected letter
    definitions = []
    if letter == '*':
        definitions = list(mongo.db.definitions.find({}))
    else:
        definitions = list(mongo.db.definitions.find({'term': {'$regex': f'^{letter}', '$options': 'i'}}))
    
    return render_template('browse.html', definitions=definitions, letter=letter)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = mongo.db.users
        user = users.find_one({'username': username})
        if user and check_password_hash(user['password'], password):
            session['user'] = str(user['_id'])
            return redirect(url_for('index'))
        else:
            return 'Invalid username or password'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

@app.route('/add_term', methods=['GET', 'POST'])
def add_term():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        term = request.form['term']
        definition = request.form['definition']
        created_by = ObjectId(session['user'])
        definitions = mongo.db.definitions
        definition_doc = {
            'term': term,
            'definition': definition,
        }
        definitions.insert_one(definition_doc)
        return redirect(url_for('index'))
    
    return render_template('add_term.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if query:
        # Perform a case-insensitive search in MongoDB
        matching_definitions = mongo.db.definitions.find({'term': {'$regex': query, '$options': 'i'}})
    else:
        # Handle case where no query is provided
        matching_definitions = mongo.db.definitions.find()
    
    return render_template('index.html', definitions=matching_definitions)

# Add this route to handle registration
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
            hash_pass = generate_password_hash(password)
            users.insert_one({'username': username, 'password': hash_pass})
            session['user'] = str(users.find_one({'username': username})['_id'])
            return redirect(url_for('index'))
        else:
            flash('Username already exists!')
            return redirect(url_for('register'))
    
    return render_template('register.html')


if __name__ == "__main__":
    app.run(host=os.environ.get("IP", "0.0.0.0"),
            port=int(os.environ.get("PORT", 5000)),
            debug=True)



