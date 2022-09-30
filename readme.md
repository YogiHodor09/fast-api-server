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

To run the fastapi in cmd Redirect to base root folder :- uvicorn books(classname):app --reload

Output in browser :
{
"message": "Hello Yogeshwar!"
}

\*\*\*\* FastAPI will return the response in JSON Format
