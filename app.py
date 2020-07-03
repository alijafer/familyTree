# coding: utf-8

import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Person, Relations
from typing import Final

# create and configure the app
app = Flask(__name__)
setup_db(app)
CORS(app)
app.config['JSON_AS_ASCII'] = False
relation_const : Final = [ "Father",
                               "Mother",
                               "wife",
                               "husbend",
                              "child"]

@app.route("/", methods=['GET'])
def persons_get_all():
    person_list = {}
    try:
        person_qurey = Person.query.all()
        for person in person_qurey:
            person_list[person.person_id] = person.format()
        print(person_list)

        return jsonify({
            "success": True,
            "persons": person_list
        })
    except Exception:
        abort(401)


@app.route("/person", methods=['POST'])
def person_insert():
    data = request.get_json()
    name = data.get('name', None)
    gender = data.get('gender', None)
    day_of_birth = data.get('day_of_birth', None)
    day_of_death = data.get('day_of_death', None)
    notes = data.get('notes', None)
    address = data.get('address', None)
    nickname = data.get('nickname', None)
    status = data.get('status', None)
    if not name:
        abort(422)
    if gender == "m" or "f" or "male" or "female":
        person = Person(
            name=name,
            gender=gender,
            day_of_birth=day_of_birth,
            day_of_death=day_of_death,
            notes=notes,
            address=address,
            nickname=nickname,
            status=status)
        person.insert()
        print(person)
        return jsonify({
            "success": True,
            "persons": name
        })
    else:
        abort(400)


@app.route('/partenr', methods=['POST'])
def make_partenr():
    data = request.get_json()
    person = data.get('person', None)
    partenr = data.get('partenr', None)
    relation = data.get('relation', None)
    #print(data)
    if type(person) is not int or person is None:
        abort(400)
    if type(partenr) is not int or partenr is None:
        abort(400)
    if type(relation) is not int or relation is None:
        abort(400)
    name_person = Person.query.filter_by(person_id=person).one_or_none()
    # print(name_person.name)
    if name_person is None:
        abort(400)
    name_partenr = Person.query.filter_by(person_id=partenr).one_or_none()
    # print(name_partenr.name)
    if name_partenr is None:
        abort(400)
    # print(relation_const[relation-1])
    relations = Relations(
      person=person,
      partenr=partenr,
      relation=relation
    )
    relations.insert()
    return jsonify({
        "success": True,
        "persons": name_person.name.format(),
        "partenr": name_partenr.name.format(),
        "relation": name_partenr.name.format()+" became the "+
        relation_const[relation-1]+" of "+name_person.name.format()
      })



# Error Handling
'''
Example error handling for unprocessable entity
'''


@app.errorhandler(422)
def unprocessable(error):
  return jsonify({
      "success": False,
      "error": 422,
      "message": "unprocessable",
      "description": "may be "
      }), 422


@app.errorhandler(404)
def unprocessable(error):
    '''
error handler for 404
    error handler is conform to general task above
    '''
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
        }), 404


@app.errorhandler(401)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": "Unauthorized",
        "description": " The server could not verify that you are" +
        " authorized to access the URL requested. You either supplied the " +
        "wrong credentials (e.g. a bad password), or your browser doesn't" +
        " understand how to supply the credentials required."
        }), 401


@app.errorhandler(400)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "bad request"
        }), 400


@app.errorhandler(500)
def bad_request(error):
    return jsonify({
      "success": False,
      "error": 500,
      "message": "Internal Server Error"
    }), 500


# @app.errorhandler(AuthError)
# def handle_auth_error(exception):
    '''
error handler for AuthError
    error handler is conform to general task above
    '''
#    response = jsonify(exception.error)
#    response.status_code = exception.status_code
#    return response


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
