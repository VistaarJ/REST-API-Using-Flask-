#!flask/bin/python
from flask import Flask
from flask.ext.restless import APIManager #Automates GET and POST requests 
from flask.ext.sqlalchemy import SQLAlchemy #Using Database SQLite
from flask.ext.cors import CORS #To enable Cross Origin Resource Sharing
from flask import render_template
from flask.ext.triangle import Triangle #to load AngularJS on Flask Server without confusion, as both use {{ }}
# from flask_restful import Resource,Api

app = Flask(__name__)
CORS(app) #will not work without CORS support in the API
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///people.db'
db = SQLAlchemy(app)
# api=Api(app)
Triangle(app) #initialises Triangle constructor

class Person(db.Model): #creates a database model for the Person object
    id = db.Column(db.Integer)
    name = db.Column(db.Text, primary_key=True) #taken to be the primary key
    phone = db.Column(db.Text)

@app.route('/') #renders the index.html file at the root directory
def index():
	return render_template('index.html',
                           title='Home')
# class Views(Resource):
# 	def index(self,todo_id):
# 		return index.html

# api.add_resource(Views,'/index.html')


db.create_all() #initialises people.db in the directory with the given column names after starting server

api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(Person, methods=['GET', 'POST', 'PATCH', 'DELETE', 'PUT'])

app.debug = True	

if __name__ == "__main__":
    app.run()