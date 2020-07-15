# Family Tree
## Introduction
A project to create a family and display it in a simple way (JSON) using Python Flask 
- [heroku url](https://famliy-tree-api.herokuapp.com/v1/)

This is backend using Flask web framework for Python
 
### `Person` has family: Parents, partner, children
api can use to make:
- Add Person
- make partner
- fix data of Person and partner
- remove partner
- delete person
## The purpose for create
I have a big family (it's really big 😓)  my uncle took it upon himself to register the entire family. This idea came to me to solve documentation and coordination problems
## Getting Started for local use
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

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) s the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in [./app.py](./app.py) and can reference [./models.py](./models.py)

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the [`./`](./)  directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:
for Windows 
```dos
set FLASK_APP=app.py
set var in setup.sh

```
for linux or macOS
```bash
. setup.sh
```
To run the server, execute:
```bash
flask run
```
or 
```bash
python app.py
```
The api will run in 5000 port

# Testing
There are two methods to test our api
- postman for test endpoint in [heroku](https://famliy-tree-api.herokuapp.com/v1/saimple)
- Using unittest [test_app.py](./test_app.py)
## Testing
To run test 
```bash
dropdb famliytree_test1 [<username>]
createdb famliytree_test1 [<username>]
psql famliytree_test1 [<username>] < test.psql
export token-admin
export token-admin-lite
python test_app.py
```
# Postman 
## This is test endpoints at live application endpoint
[Postman](https://www.postman.com/) is software to test endpoints 
Just import [famliytree.postman_collection.json](./famliytree.postman_collection.json) into postman software

or 

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/4289ad641f0e6109bdb5)

if get 401 please email me to give you a new token

if you have new token please update authorization Bearer.Token in Admin and lite admin `(hint click right on Admin folder then click edit)`

if get any error expet 401 chake the int:id in databess
let's to play :metal

will test the Heroku Deployment
## Variables
- host: https://famliy-tree-api.herokuapp.com/v1

    `if you need test in locally change Variables to you local host url`
# Auth0
This project use Auth0 to manage authorization use endpoints.
in the table below explained which roles get permission to access endpoints.
Permission(Scopes)\Roles |familyAdmin | liteAdminFamily | userFamily
--- | --- | --- | --- |
get:person | ● | ● | ● 
get:partenr | ● | ● | ● 
post:person | ● | ● | X 
post:partenr | ● | ● | X 
patch:person | ● | X | X 
patch:partenr | ● | X | X
delete:partenr | ● | X | X
delete:person | ● | X | X

# Endpoints explained
VERSION is `v1`

 ## GET /saimple
- Fetches five names of persons
- Returns first 5 name person and 200
- public 
- Request Arguments: None

<details>
<summary>Sample:</summary>


 ```curl
curl -L -X GET 'https://famliy-tree-api.herokuapp.com/v1/saimple'
```
- Respons:
```json
{
    "persons": [
        {
            "name": "abdalah"
        }
    ],
    "success": true
}
```
</details>

 ## GET /person
- Fetches  information of persons
- Returns 3 person in each page, and 200 success
- privet 
- Scope get:person
- Request Arguments:
 `
    'Authorization': 'Bearer '+ token
`

<details>
<summary>Sample:</summary>

 ```cURL
curl -L -X GET 'https://famliy-tree-api.herokuapp.com/v1/person' -H 'Authorization: Bearer Token'
```
- Respons:
```json
{
    "persons": [
        {
            "address": "ahsaa",
            "day_of_birth": 1930,
            "day_of_death": 2018,
            "gender": "m",
            "name": "abdalah",
            "nickname": "bo mohammad",
            "notes": "test",
            "person_id": 1,
            "status": "death"
        }
    ],
    "success": true
}
```
</details>

## GET /relation
- Fetches information of relations
- Returns 3 relations in each page, and 200 success
- privet 
- Scope get:partenr
- Request Arguments:
 `
    'Authorization': 'Bearer '+ token
`
<details>
<summary>Sample:</summary>


 ```cURL
curl -L -X GET 'https://famliy-tree-api.herokuapp.com/v1/relation' -H 'Authorization: Bearer Token'
```
- Respons:
```json
{
  "persons": [
    {
      "partenr": 3,
      "person": 2,
      "relation": 4,
      "relation_id": 1
    },
    {
      "partenr": 2,
      "person": 3,
      "relation": 3,
      "relation_id": 2
    },
    {
      "partenr": 3,
      "person": 1,
      "relation": 1,
      "relation_id": 3
    }
  ],
  "success": true
}
```
</details>

 ## GET /partenr/`<int:id>`
 - Fetches family;  id_partenr person that
respons all person has id partern in partenr from Relation table 

- Returns father and mother of child, all person information has same partenr id, and 200 success
- privet
- Scope get:partenr
- Request Arguments:
 ```json
 id: int [relation_id] 
'Authorization': 'Bearer '+ token
```

<details>

<summary>Sample:</summary>

```curl
curl -L -X GET 'https://famliy-tree-api.herokuapp.com/v1/partenr/0' -H 'Authorization: Bearer
```
- Respons:
```json 
{
    "data": {
        "2": {
            "partenr": {
                "address": "ahsaa",
                "day_of_birth": 1930,
                "day_of_death": 2018,
                "gender": "m",
                "name": "abdalah",
                "nickname": "bo mohammad",
                "notes": "test",
                "person_id": 1,
                "status": "death"
            },
            "partenrid": 1,
            "person": {
                "address": "ahsaa",
                "day_of_birth": 1994,
                "day_of_death": null,
                "gender": "m",
                "name": "ali",
                "nickname": "bo jafer",
                "notes": "test",
                "person_id": 2,
                "status": "live"
            },
            "relation": 1
        }
    },
    "id_partenr": 1,
    "relations": {
        "1,2": {
            "2": {
                "address": "ahsaa",
                "day_of_birth": 1994,
                "day_of_death": null,
                "gender": "m",
                "name": "ali",
                "nickname": "bo jafer",
                "notes": "test",
                "person_id": 2,
                "status": "live"
            },
            "partenr": {
                "address": "ahsaa",
                "day_of_birth": 1930,
                "day_of_death": 2018,
                "gender": "m",
                "name": "abdalah",
                "nickname": "bo mohammad",
                "notes": "test",
                "person_id": 1,
                "status": "death"
            },
            "partenrid": 1,
            "relation": 1
        }
    },
    "success": true
}
```
</details>

 ## POST /person
 - create and insert person
- Returns name of person, and 200 success
- privet 
- Scopes: person:post 
- Request Arguments:
 ```json
    'Authorization': 'Bearer '+ token
    -H 'Content-Type: application/json'
     --data-raw '{
    "name": string,
    "gender": String [m, f, male, female],
    "day_of_birth": int,
    "day_of_death": int,
    "notes": string,
    "address": string,
    "nickname": string,
    "status": string
     }
```

`I use int in day_of_birth, day_of_death just for simplete to deal with data. in the next version the type will be converted to a date/time`

<details>

<summary>Sample:</summary>

```curl
curl -L -X POST 'https://famliy-tree-api.herokuapp.com/v1/person' -H 'Authorization: Bearer Token' -H 'Content-Type: application/json' --data-raw '{
    "name": "ali",
    "gender": "m",
    "day_of_birth": 1994,
    "day_of_death":None,
    "notes": "test",
    "address": "ahsaa",
    "nickname": "bo mohammad",
    "status": "live"
}'
```
- Respons:
```json 
{
    "persons": "ali",
    "success": true
}
```
</details>

 ## POST /partenr
 - create and make partenr
 make realtion between two person every person has partenr
- Returns name of person, name of partenr, message descripe relation status and 200 success
- privet
- post:partenr
- Request Arguments:
 ```json
    'Authorization': 'Bearer '+ token
    -H 'Content-Type: application/json'
     --data-raw '{
    "partenr": int,
    "person": int,
    "relation": int
     }
```
<details>

<summary>Sample:</summary>
 
```curl
curl -L -X POST 'https://famliy-tree-api.herokuapp.com/v1/partenr' -H 'Authorization: Bearer Token' -H 'Content-Type: application/json' --data-raw '{
    "partenr": 1,
    "person": 2,
    "relation": 1
}'
```
- Respons:
```json 
{
    "partenr": "abdalah",
    "person": "ali",
    "relation": "abdalah became the Father of ali",
    "success": true
}
```

</details>

## DELETE /partenr/`<int:id>`
 - delete relastion, remove partenr
- Returns delete_id, message, relation, success 200
- privet
- delete:partenr
- Request Arguments:
 ```json
 id: int [relation_id] 
'Authorization': 'Bearer '+ token
```
<details>

<summary>Sample:</summary>
 
```curl
curl -L -X DELETE 'https://famliy-tree-api.herokuapp.com/v1/partenr/2' -H 'Authorization: Bearer Token' -H 'Content-Type: application/json' 
```
- Respons:
```json 
{
    "delete_id": 2,
    "message": "Relations successfully deleted",
    "relation": "test child relationship with ali's was separated",
    "success": true
}
```

</details>


## DELETE /person/`<int:id>`
 - delete person
- Returns delete_id, message, relation, success 200
- privet
- scope delete:person
- Request Arguments:
 ```json
 id: int [person_id] 
'Authorization': 'Bearer '+ token
```
<details>

<summary>Sample:</summary>
 
```curl
curl -L -X DELETE 'https://famliy-tree-api.herokuapp.com/v1/person/3' -H 'Authorization: Bearer Token' -H 'Content-Type: application/json' 
```
- Respons:
```json 
{
    "delete_id": 3,
    "message": "test (Person) successfully deleted",
    "success": true
}
```
</details>


## PATCH /person/`<int:id>`
 - update person
- Returns name of person, and 200 success
- privet
- scope patch:person
- Request Arguments:
 ```json
 id: int [person_id] 
'Authorization': 'Bearer '+ token
    --data-raw '{
    "gender": string,
    "name": string,
    "notes": string,
    "day_of_birth": int,
    "day_of_death": int,
    "address": string,
    "nickname": string,
    "status": string
}'
```

<details>

<summary>Sample:</summary>
 
```curl
curl -L -X PATCH 'https://famliy-tree-api.herokuapp.com/v1/person/2' -H 'Authorization: Bearer Token' -H 'Content-Type: application/json' 
--data-raw '{
    "person_id": ,
    "gender": "f",
    "name": "zinab",
    "notes": "chees",
    "day_of_birth": 2006,
    "day_of_death": 2050,
    "address": "address",
    "nickname": "nickname",
    "status": "status"
}'
```
- Respons:
```json 
{
    "persons": "zinab",
    "success": true
}
```

</details>

## PATCH /partenr/`<int:id>`
 - update relastion
- Returns name of person, and 200 success
- privet
- scope patch:partenr
- Request Arguments:
 ```json
id: int [relation_id] 
'Authorization': 'Bearer '+ token
--data-raw '{
    "partenr": int,
    "person": int,
    "relation": int
}'
```
<details>

<summary>Sample:</summary>

```curl
curl -L -X PATCH 'https://famliy-tree-api.herokuapp.com/v1/partenr/3' -H 'Authorization: Bearer Token' -H 'Content-Type: application/json' 
--data-raw '{
    "partenr": 2,
    "person": 4,
    "relation": 4
}'
```

- Respons:

```json 
{
    "partenr": "ali",
    "persons": "zinab",
    "relation": "ali became the husband of zinab",
    "success": true
}
```
</details>

## Error Handling
Errors are returned in the following json format:
```
{
  "error": 400,
  "message": "bad request",
  "success": false
}
```
HTTP response status codes currently returned are:
- 404 : resource not found
- 422 : unprocessable
- 400 : bad request
- 500 : Internal Server Error
- 401 : authorization_header_missing
# Author
Ali J. Alamer
# Acknowledgements
This is the end of trip 🐱‍🏍 in Full-Stack Developer Nanodegree Program 👨‍🎓
I thanks Udacity 😇 to help me learn ✍ Flask. Also I thanks Misk for giving me this opportunity to enter this course 📚.