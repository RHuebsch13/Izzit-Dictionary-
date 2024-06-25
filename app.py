import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")
@app.route('/')
def home():
    letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]  # List of letters A-Z
    terms = list(mongo.db.definitions.find().sort("term", 1))  # Fetch all terms sorted alphabetically
    return render_template('index.html', terms=terms, letters=letters)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_query = request.form.get('search_query')
        terms = list(mongo.db.definitions.find({"term": {"$regex": search_query, "$options": "i"}}).sort("term", 1))
        return render_template('index.html', terms=terms)
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP", "0.0.0.0"),
            port=int(os.environ.get("PORT", 5000)),
            debug=True)
