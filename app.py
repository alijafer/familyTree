# coding: utf-8

import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Person, Relations
from typing import Final
from utilies import paginate_person


def create_app():
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    app.config['JSON_AS_ASCII'] = False
    relation_const : Final = [ "Father",
                                "Mother",
                                "wife",
                                "husband",
                                "child"]
    PERSONS_PER_PAGE = 3
    version  : Final = "v1"

    @app.route("/"+version+"/person", methods=['GET'])
    def persons_get_all():
        person_list = {}
        try:
            person_qurey = Person.query.all()
            current_persons = paginate_person(request, person_qurey, PERSONS_PER_PAGE)
            ''' for person in person_qurey:
                person_list[person.person_id] = person.format()
            print(person_list) '''
            if (len(current_persons) == 0):
                abort(404)
            return jsonify({
                "success": True,
                "persons": current_persons
            })
        except Exception:
            abort(404)


    @app.route("/"+version+"/person", methods=['POST'])
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


    @app.route("/"+version+'/partenr', methods=['POST'])
    def make_partenr():
        data = request.get_json()
        person = data.get('person', None)
        partenr = data.get('partenr', None)
        relation = data.get('relation', None)
        #print(data)
        if type(person) is not int or person is None or person <= 0:
            abort(422)
        if type(partenr) is not int or partenr is None or partenr <= 0:
            abort(422)
        if partenr == person:
            abort(404)
        if type(relation) is not int or relation is None or relation > 5 \
            or relation <= 0:
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
        temp = ""
        if relation >= 5:
            temp = name_person.name.format()+" became the "+\
            relation_const[relation-1]+" of "+name_partenr.name.format()
        else:
            temp = name_partenr.name.format()+" became the "+\
            relation_const[relation-1]+" of "+name_person.name.format()
        return jsonify({
            "success": True,
            "persons": name_person.name.format(),
            "partenr": name_partenr.name.format(),
            "relation": temp
        })


    @app.route("/"+version+"/partenr/<int:id_partenr>", methods=['GET'])
    def persons_get_partenr(id_partenr):
        print("aa")
        if id_partenr == 0:
            partenr_father_query = Relations.query.filter_by(relation=1).all()
            person_short = Person.query.all()
            short_person = [personn.short() for personn in person_short]
            #sh = set(short_person)
            print(short_person[1])
            #print(sh)
            #print(partenr_father_query)
            #p = paginate_person(request, partenr_father_query, PERSONS_PER_PAGE)
            person_list = []
            chiled_list = []
            alls = []
            for partenr in partenr_father_query:
                person_list.append(Person.query.filter_by(person_id=partenr.partenr).first())
                chiled_list.append(Person.query.filter_by(person_id=partenr.person).first())

            #print(person_list)
            print(chiled_list)
            p = paginate_person(request, person_list, PERSONS_PER_PAGE)
            o = paginate_person(request, chiled_list, PERSONS_PER_PAGE)
            print(person_list)
            #person_father_query = Person.query.filter_by(person_id=person_list).first()
            #print(person_father_query)
            return jsonify({
            "success": True,
            "all": "aa",
            "p": short_person,
            "o": o
            })
        else:
            partenr_father_query = Relations.query.filter_by(relation=1).all()
            person_short = Person.query.all()
            short_person = [personn.short() for personn in person_short]


    @app.route("/"+version+'/partenr/<int:id>', methods=['DELETE'])
    def remove_partenr(id):
        if id is None or id == 0:
            abort(404)
        partenr = Relations.query.filter_by(relation_id=id).one_or_none()
        if partenr is None:
            abort(404)
        try:
            partenr_format = partenr.format()
            relation = partenr_format.get("relation")
            id_person = partenr_format.get("person")
            id_partenr = partenr_format.get("partenr")
            name_person = Person.query.filter_by(person_id=id_person).one_or_none()
            name_partenr = Person.query.filter_by(person_id=id_partenr).one_or_none()
            temp = ""
            ''' Ahmed's relationship with Fatima's husband was separated '''
            if relation >= 5:
                temp = name_person.name.format()+" "+relation_const[relation-1]+\
                    " relationship with "+ name_partenr.name.format()+"'s "+\
                    "was separated"
            else:
                temp = name_partenr.name.format()+" relationship with "+\
                name_person.name.format()+"'s "+relation_const[relation-1]+\
                    " was separated"
            partenr.delete()
            return jsonify({
                "success": True,
                "delete_id": id,
                'message': "Relations successfully deleted",
                "relation": temp
            })
        except Exception:
            abort(422)

    @app.route("/"+version+'/person/<int:id>', methods=['DELETE'])
    def person_delete(id):
        if id is None or id == 0:
            abort(404)
        person = Person.query.filter_by(person_id=id).one_or_none()
        if person is None:
            abort(404)
        person_format = person.format()
        person_name = person_format.get("name")
        try:
            person.delete()
            return jsonify({
                "success": True,
                "delete_id": id,
                'message': person_name+" (Person) successfully deleted",
            })
        except Exception:
            abort(422)


    @app.route("/"+version+'/person/<int:id>', methods=['PATCH'])
    def person_fix_data(id):
        if id is None or id == 0:
            abort(404)
        person = Person.query.filter_by(person_id=id).one_or_none()
        if person is None:
            abort(404)
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
            try:
                person.name = name
                person.gender = gender
                person.day_of_birth = day_of_birth
                person.day_of_death = day_of_death
                person.notes = notes
                person.address = address
                person.nickname = nickname
                person.status = status
                #persons.person_id = person_id
                person.update()
                #print(person)
                return jsonify({
                    "success": True,
                    "persons": name
                })
            except Exception:
                abort(422)
        else:
            abort(400)


    @app.route("/"+version+'/partenr/<int:id>', methods=['PATCH'])
    def partenr_fix_data(id):
        if id is None or id == 0:
            abort(404)
        print(id)
        relations = Relations.query.filter_by(relation_id=id).one_or_none()
        if relations is None:
            abort(404)
        data = request.get_json()
        person = data.get('person', None)
        partenr = data.get('partenr', None)
        relation = data.get('relation', None)
        #print(data)
        if type(person) is not int or person is None or person <= 0:
            abort(422)
        if type(partenr) is not int or partenr is None or partenr <= 0:
            abort(422)
        if partenr == person:
            abort(422)
        if type(relation) is not int or relation is None or relation > 5 \
            or relation <= 0:
            abort(422)
        name_person = Person.query.filter_by(person_id=person).one_or_none()
        # print(name_person.name)
        if name_person is None:
            abort(422)
        name_partenr = Person.query.filter_by(person_id=partenr).one_or_none()
        # print(name_partenr.name)
        if name_partenr is None:
            abort(422)
        # print(relation_const[relation-1])
        try:
            relations.person = person
            relations.partenr = partenr
            relations.relation = relation
            relations.update()
            temp = ""
            if relation >= 5:
                temp = name_person.name.format()+" became the "+\
                relation_const[relation-1]+" of "+name_partenr.name.format()
            else:
                temp = name_partenr.name.format()+" became the "+\
                relation_const[relation-1]+" of "+name_person.name.format()
            return jsonify({
                "success": True,
                "persons": name_person.name.format(),
                "partenr": name_partenr.name.format(),
                "relation": temp
            })
        except Exception:
            abort(422)
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
    return app
 

   
