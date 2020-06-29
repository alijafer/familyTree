# Family Tree 
## A project to create a family tree and display it in a simple way using Python Flask 

This is backend using Flask web framework for Python

### `Person` has family: Parents, grandba, grandma, partner, children


## Getting Started
### Installing Dependencies
#### Python 3.8
Follow instructions to install the latest version of python for your platform in the [python docs](https://www.python.org/downloads/)
#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.
##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) s the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in `./app.py` and can reference `./models.py`

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the `./`  directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:
for Windows 
```bash
set FLASK_APP=app.py
```
for linux or macOS
```bash
export FLASK_APP=api.py;
```


# Author
Ali J. Alamer 