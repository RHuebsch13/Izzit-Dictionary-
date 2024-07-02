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
    # Fetch all definitions
    all_definitions = mongo.db.definitions.find()
    return render_template('index.html', definitions=all_definitions)

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

if __name__ == "__main__":
    app.run(host=os.environ.get("IP", "0.0.0.0"),
            port=int(os.environ.get("PORT", 5000)),
            debug=True)



