Test python code using pylint:
pylint (classname).py -r y

# DOWNLOAD THE SOURCE CODE PROJECT :

GIT CLONE -

# git clone https://github.com/codingwithroby/fastapi-the-complete-course.git

CMDS AFTER DOWNLOADING THE SOURCE CODE EXAMPLE :

# pip install -r requirements.txt

# INSTALLS ALL THE REQUIRED DEPENDENCIES

========================

Install FastAPI

To check Pip version :-

# python -m pip --version

pip list :- To list the packages installed by pip manager in python.

To install virtualenv :-

# pip install virtualenv

To create the FastAPI virtual environment :-

# python -m venv fastapienv

To activate the fastapienv / cmd :-

# Redirect to FastAPI project folder -> fastapienv-> Scripts -> activate

To de-activate the env /cmd :-

# Redirect to FastAPI project folder -> fastapienv-> Scripts -> deactivate

To install all dependencies for FastAPI:-

# pip install fastapi[all]

# unicorn is another dependency for fastapi development like fastapi , virenv

# https://www.uvicorn.org/

# UVICORN - TO REGISTER OUR SERVER WITH ASGI

To run the fastapi in cmd Redirect to base root folder :-

# uvicorn (classname):app --reload

# --reload :- TO restart the server used in Development server not in Production server

Output in browser :
{
"message": "Hello Yogeshwar!"
} // \*\*\*\* FastAPI will return the response in JSON Format

# To see openapi schema url / your endpoint:-

# http://127.0.0.1:8000/openapi.json

# To view SwaggerUI right away for our rest API created :-

# http://127.0.0.1:8000/docs

===================================
ENDPOINTS METHODS EXPLANATION FOR :

# HTTP REQUEST METHODS

get() - Read method that retrieves data
post() - Create method , to submit data
put() - Update the entire resource
patch() - Update the part of resource
delete() - Delete the resource

# FASTAPI ADDITIONAL HTTP REQUEST METHODS

trace() - Performs a message loop-back to the target
options() - Describes communication options to the target
connect() - Create a tunnel to the server , based on the target resource

# FASTAPI HTTP RESPONSE STATUS CODES

100 - Informational response : Request processing.
200 - Success : Request successfully completed
300 - Redirection : Further action must be complete
400 - Client errors : An error caused by the request from the client (syntax not understandable by the server from the
client)
500 - Server errors : An error has occurred in the server

=====================================

# TO MAKE QUERY PARAM OPTIONAL

@get('/etc')
def (str : Optional[str])

# TO ASSIGN QUERY PARAMS IN DECORATOR

# BY DEFAULT POST AND PUT METHOD VARIABLES IS TAKEN AS QUERY PARAMS

# @get('/assign/') -> '/ at the end denotes that this end point accepts Query Param.'

# TO INSTALL SQL ALCHEMY FOR SQL CONNECTION AND MANAGEMENT :

# pip install sqlalchemy

====================================

# TO CREATE A DB IN FASTAPI:

Step 1:-

1. Create Engine based DB Url
2. Create DB Session
3. Create Base class for DB Models

Step 2:-

1. Create Model class for Columns for DB Table created.

Step 3:-

1. In main.py file = Create instance for model created with Base and Bind Engine

# To run the sqlite3 DB in Terminal

# or in DB Browser App for sqlite :-

Project Folder -> sqlite3 dbname.db

CMDS :-
Terminal ->
.schema
.mode (o/p mode for display) eg: .mode column

=======================================

# CREATE HASH PASSWORD LIB :

pip install "passlib[bcrypt]"

# import Depends from FastAPI - Create DB Functions

# import Password Bearer for token:

pip install "python-jose[cryptography]"
