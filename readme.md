Test python code using pylint:
pylint myexample.py -r y

========================
Install FastAPI

To check Pip version :- python -m pip --version

pip list :- To list the packages installed by pip manager in python.

To install virtualenv :- pip install virtualenv

To create the FastAPI virtual environment :- python -m venv fastapienv

To activate the fastapienv / cmd :- Redirect to FastAPI project folder -> fastapienv-> Scripts -> activate
To de-activate the env /cmd :- Redirect to FastAPI project folder -> fastapienv-> Scripts -> deactivate

To install all dependencies for FastAPI:- pip install fastapi[all]

# unicorn is another dependency for fastapi development like fastapi , virenv

# https://www.uvicorn.org/

# UVICORN - TO REGISTER OUR SERVER WITH ASGI

To run the fastapi in cmd Redirect to base root folder :- uvicorn (classname):app --reload

# --reload :- TO restart the server used in Development server not in Production server

Output in browser :
{
"message": "Hello Yogeshwar!"
} // \*\*\*\* FastAPI will return the response in JSON Format

To see openapi schema url / your endpoint:-

# http://127.0.0.1:8000/openapi.json

To view SwaggerUI right away for our rest API created :-

# http://127.0.0.1:8000/docs

===================================
ENDPOINTS METHODS EXPLANATION FOR :

# HTTP REQUEST METHODS

get() - Read method that retreives data
post() - Create method , to submit data
put() - Update the entire resource
patch() - Update the part of resource
delete() - Delete the resource

# FASTAPI ADDTIONAL HTTP REQUEST METHODS

trace() - Performs a message loop-back to the target
options() - Describes communication options to the target
connect() - Create a tunnel to the server , based on the target resource

# FASTAPI HTTP RESPONSE STATUS CODES

100 - Informational response : Request processing.
200 - Success : Request successfully completed
300 - Redirection : Further action must be complete
400 - Client errors : An error caused by the request from the client (syntax not understandable by the server from the client)
500 - Server errors : An error has occurred in the server

=====================================
