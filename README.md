# REST-API-Using-Flask

##Installation Instructions

Create a directory to hold the project

    mkdir myproject
    cd myproject

Clone the directory 

    git clone https://github.com/VistaarJ/REST-API-Using-Flask-

Go to the directory 

    cd REST-API-Using-Flask-
  
Activate virtual environment

    . venv/bin/activate
  
Install the required dependencies

    pip install Flask
    pip install Flask-restless
    pip install Flask-sqlalchemy
    pip install Flask-cors
    pip install flask-triangle 
    
You are now ready to go!

Setup the people.db database with whatever values you want

Deploy the server

    python ./app.py
   
    http://localhost:5000/api/person should contain the entire list of people (with id,name and phone numbers) in JSON format
    http://localhost:5000/api/person/Name_of_person contains JSON response for person with Name as Name_of_person
   
To see output using AngularJS in tabular format, open the index.html file in the REST-API-Using-Flask- directory using Firefox

##Requests

To do GET and POST requests on the database while it is deployed, use 

####GET requests

    curl -X GET http://localhost:5000/api/person
    curl -X GET http://localhost:5000/api/person/Name_of_person

or alternatively

    GET http://localhost:5000/api/person
    GET http://localhost:5000/api/person/Name_of_person

Returns a JSON request to the Command Line

####POST requests

    curl -X POST -H "Content-Type: application/json" -d '{"id":"101", "name":"Person to be added", "phone":"1111111111"}' http://localhost:5000/api/person
(id is optional, if not given, it will be taken as null)

Inserts into the SQLite database with values (101,"Person to be added", "1111111111")

or alternatively

    POST -H "Content-Type: application/json" http://localhost:5000/api/person

and then enter the POST data as

    {"id":"101", "name":"Person to be added", "phone":"1111111111"}








