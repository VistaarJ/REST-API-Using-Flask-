#!flask/bin/python
from flask import Flask
from flask.ext.restless import APIManager #Automates GET and POST requests 
from flask.ext.sqlalchemy import SQLAlchemy #Using Database SQLite
from flask.ext.cors import CORS #To enable Cross Origin Resource Sharing

app = Flask(__name__)
CORS(app) #will not work without CORS support in the API
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///people.db'
db = SQLAlchemy(app)

class Person(db.Model): #creates a database model for the Person object
    id = db.Column(db.Integer)
    name = db.Column(db.Text, primary_key=True) #taken to be the primary key
    phone = db.Column(db.Text)

db.create_all() #initialises people.db in the directory with the given column names after starting server

api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(Person, methods=['GET', 'PUT', 'POST'])

app.debug = True	

if __name__ == "__main__":
    app.run()