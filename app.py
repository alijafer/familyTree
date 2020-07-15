# coding: utf-8

import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Person, Relations
from utilies import paginate_person
from auth import AuthError, requires_auth


''' This's api for store and retrieve Family data information like name,
 relation between two persons '''


def create_app():
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    app.config['JSON_AS_ASCII'] = False
    # Relation const is final(fixed) for values for relationships
    RELATION_CONST = ["Father", "Mother", "wife", "husband", "child"]
    # PERSONS_PER_PAGE how many persons send per page
    PERSONS_PER_PAGE = 3
    # version of api
    VERSION = "v1"

    @app.route("/"+VERSION+"/saimple", methods=['GET'])
    def persons_get_short_five():
        '''
        Displaying five names of persons
        return 5 name person and 200
        public / get methods
        select name from Person limit 5
        if any problem raise 404 like no data
        '''
        person_list = {}
        try:
            person_qurey = Person.query.limit(5).all()
            short_person = [personn.shortName() for personn in person_qurey]
            if (len(short_person) == 0):
                abort(404)
            return jsonify({
                "success": True,
                "persons": short_person
            })
        except Exception:
            abort(404)

    @app.route("/"+VERSION+"/person", methods=['GET'])
    @requires_auth('get:person')
    def persons_get_all(payload):
        '''
        send all persons information from databeass
        privet /person get methods
        each page send 3 persons
        scope requires authtction get:person
        select * from person
        return 3 person in each page, and 200 success
        if any problem raise 404 like no data
        '''
        person_list = {}
        try:
            person_qurey = Person.query.all()
            current_persons = paginate_person(request, person_qurey,
                                              PERSONS_PER_PAGE)
            if (len(current_persons) == 0):
                abort(404)
            return jsonify({
                "success": True,
                "persons": current_persons
            })
        except Exception:
            abort(404)

    @app.route("/"+VERSION+"/relation", methods=['GET'])
    @requires_auth('get:partenr')
    def partenr_get_all(payload):
        '''
        send all relation information from databeass
        privet /relation get methods
        each page send 3 relation
        scope requires authtction get:partenr
        select * from relation
        return 3 relation in each page, and 200 success
        if any problem raise 404 like no data
        '''
        person_list = {}
        try:
            partenr_qurey = Relations.query.all()
            current_partenr = paginate_person(request, partenr_qurey,
                                              PERSONS_PER_PAGE)
            if (len(current_partenr) == 0):
                abort(404)
            return jsonify({
                "success": True,
                "relation": current_partenr
            })
        except Exception:
            abort(404)

    @app.route("/"+VERSION+"/person", methods=['POST'])
    @requires_auth('post:person')
    def person_insert(payload):
        '''
        create and insert person
        privet /person post methods
        get data (name, gender, day_of_birth, day_of_death, notes, address,
         nickname, status) from json requst then insert data into person object
        scope requires authtction post:person
        insert into person (name, gender, day_of_birth, day_of_death, notes,
         address, nickname, status) VALUES /*from json requst*/(name, gender,
          day_of_birth,day_of_death, notes, address, nickname, status)
        return name of person, and 200 success
        if any problem in name raise 422 if gender not m, f, male, female raise
        400
        '''
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
            return jsonify({
                "success": True,
                "persons": name
            })
        else:
            abort(400)

    @app.route("/"+VERSION+'/partenr', methods=['POST'])
    @requires_auth('post:partenr')
    def make_partenr(payload):
        '''
        create and make partenr
        make realtion between two person every person has partenr for example:
        Ali (person) has jafer (partenr), jafer is father (relation =1) of Ali
        privet /partenr post methods
        get data (person:int, partenr:int, relation:int) from json requst then
         insert data into partenr object
        scope requires authtction post:partenr
        insert into partenr (person, partenr, relation) VALUES /*from json
         requst*/(person, partenr, relation)
        return name of person (Ali), name of partenr, message descripe relation
         of relation status and 200 success
        if any problem in id person, id partenr raise 422, if relation not int
         or above 5 or under 1 or None raise 422, if name person, name partenr
          not existing raise 400
        relation={
            1: "Father",
            2: "Mother",
            3: "wife",
            4: "husband",
            5: "child"
        }
        '''
        data = request.get_json()
        person = data.get('person', None)
        partenr = data.get('partenr', None)
        relation = data.get('relation', None)
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
        if name_person is None:
            abort(400)
        namePartenr = Person.query.filter_by(person_id=partenr).one_or_none()
        if namePartenr is None:
            abort(400)
        relations = Relations(
            person=person,
            partenr=partenr,
            relation=relation)
        relations.insert()
        message = ""
        if relation >= 5:
            message = name_person.name.format() + " became the " +\
                RELATION_CONST[relation-1] + " of " + namePartenr.name.format()
        else:
            message = namePartenr.name.format()+" became the " +\
                RELATION_CONST[relation-1] + " of " + name_person.name.format()
        return jsonify({
            "success": True,
            "person": name_person.name.format(),
            "partenr": namePartenr.name.format(),
            "relation": message
        })

    @app.route("/"+VERSION+"/partenr/<int:id_partenr>", methods=['GET'])
    @requires_auth('get:partenr')
    def persons_get_partenr(payload, id_partenr):
        '''
        Fetches family of id_partenr person
        respons all person has id partern in partenr from Relation table
         that means will return father and mother of child
        int:person has int:partenr and int:relation
        will be return all person information has same partenr id for example:
        father=jafer(partenr=id_partenr) has
            -zahar (person) relation (4)
            -and Ali (person) relation (1)
            -and Alaa (person) relation (1)
        relation={
            1: "Father",
            2: "Mother",
            3: "wife",
            4: "husband",
            5: "child"
        }
        privet /partenr/int:id_partenr get methods
        scope requires authtction get:partenr
        prtenr_father_que = select * from Relations where partenr=id_partenr
        father_format = is prtenr_father_que format from Relation object
        person = select * from Person where person_id=father_format.person
        partenr = select * from Person where person_id=father_format.partenr
        person_list is Dictionaries of person, partenr, relation
        person_list_forma is convert person_list.person, person_list.partenr to
        format, the output for each person information has partern information
        and relation:int
        relations is Dictionaries of each relation person information and
         partenr information
        return data=person_list_forma, relations=relations, id_partenr and 200
        if id_partenr = 0 raise 422, if prtenr_father_que = 0 raise 422
        '''
        if id_partenr == 0:
            abort(422)
        prtenr_father_que = Relations.query.filter_by(partenr=id_partenr).all()
        if len(prtenr_father_que) == 0:
            abort(422)
        father_format = [father_.format() for father_ in prtenr_father_que]
        person_list = {}
        for i in father_format:
            person_list[i.get('person')] = {
                'person': Person.query.filter_by(person_id=i.get('person'))
                .all(), 'relation': i.get('relation'), 'partenr': Person.query.
                filter_by(person_id=i.get('partenr')).all(),
                'relation': i.get('relation'), 'partenrid': i.get('partenr')}
        person_list_forma = {}
        for i in person_list:
            person_list_forma[i] = {
                'person': person_list[i].get('person')[0].format(),
                'relation': person_list[i].get('relation'),
                'partenrid': person_list[i].get('partenrid'),
                'partenr': person_list[i].get('partenr')[0].format()}
        relations = {}
        key_for_relation = ""
        for i in person_list_forma:
            key_for_relation = str(person_list_forma[i].get('relation')) + ','\
                + str(person_list[i].get('person')[0].person_id)
            relations[key_for_relation] = {
                str(person_list[i].get('person')[0].person_id):
                person_list[i].get('person')[0].format(),
                'relation': person_list[i].get('relation'),
                'partenrid': person_list[i].get('partenrid'),
                'partenr': person_list[i].get('partenr')[0].format()}
        return jsonify({
            "success": True,
            "data": person_list_forma,
            "relations": relations,
            "id_partenr": id_partenr
        })

    @app.route("/"+VERSION+'/partenr/<int:id>', methods=['DELETE'])
    @requires_auth('delete:partenr')
    def remove_partenr(payload, id):
        '''
        delete relastion
        privet /partenr/int:id delete methods
        scope requires authtction delete:partenr
        id is relation_id
        relation from partenr.relation
        id_person from partenr.person
        id_partenr from partenr.partenr
        partenr = select * from Relations where relation_id=id
        name_person = select * from person where person_id=id_person
        name_partenr = select * from person where person_id=id_partenr
        relation message: Ahmed's relationship with Fatima's husband was
         separated
        return delete_id, message, relation, success 200
        if any problem in id relation_id raise 404, partenr raise 404,
        if any problem when delete raise 422
        relation={
            1: "Father",
            2: "Mother",
            3: "wife",
            4: "husband",
            5: "child"
        }
        '''
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
            name_person = Person.query.filter_by(person_id=id_person).\
                one_or_none()
            name_partenr = Person.query.filter_by(person_id=id_partenr).\
                one_or_none()
            message = ""
            ''' Ahmed's relationship with Fatima's husband was separated '''
            if relation >= 5:
                message = name_person.name.format() + " " + RELATION_CONST[
                    relation-1] + " relationship with " + name_partenr.name\
                    .format()+"'s " + "was separated"
            else:
                message = name_partenr.name.format() + " relationship with " +\
                    name_person.name.format() + "'s " +\
                    RELATION_CONST[relation-1] + " was separated"
            partenr.delete()
            return jsonify({
                "success": True,
                "delete_id": id,
                'message': "Relations successfully deleted",
                "relation": message
            })
        except Exception:
            abort(422)

    @app.route("/"+VERSION+'/person/<int:id>', methods=['DELETE'])
    @requires_auth('delete:person')
    def person_delete(payload, id):
        '''
        delete person
        privet /person/int:id delete methods
        scope requires authtction delete:person
        id is person_id
        person = select * from person where person_id=id
        relation message: Ahmed's (Person) successfully deleted
        return delete_id, message, success 200
        if any problem in id raise 404, person raise 404,
        if any problem when delete raise 422
        '''
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

    @app.route("/"+VERSION+'/person/<int:id>', methods=['PATCH'])
    @requires_auth('patch:person')
    def person_fix_data(payload, id):
        '''
        update person
        privet /person/int:id PATCH methods
        scope requires authtction patch:person
        id is person_id
        person = select * from person where person_id=id
        get data (name, gender, day_of_birth, day_of_death, notes, address,
         nickname, status) from json requst then insert data into person object
         UPDATE person set  name, gender, day_of_birth, day_of_death, notes,
         address, nickname, status where person.person_id=id
        return name of person, and 200 success
        if any problem in name raise 422 if gender not m, f, male, female raise
        400, if any problem in update will raise 422
        '''
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
                person.update()
                return jsonify({
                    "success": True,
                    "persons": name
                })
            except Exception:
                abort(422)
        else:
            abort(400)

    @app.route("/"+VERSION+'/partenr/<int:id>', methods=['PATCH'])
    @requires_auth('patch:partenr')
    def partenr_fix_data(payload, id):
        '''
        update relastion
        privet /partenr/int:id patch methods
        scope requires authtction patch:partenr
        id is relation_id
        get data (person:int, partenr:int, relation:int) from json requst then
         insert data into partenr object
        scope requires authtction post:partenr
        update partenr set person, partenr, relation where relation_id=id
        relation from partenr.relation
        id_person from partenr.person
        id_partenr from partenr.partenr
        partenr = select * from Relations where relation_id=id
        name_person = select * from person where person_id=id_person
        name_partenr = select * from person where person_id=id_partenr
        relation message: Ahmed's relationship with Fatima's husband was
         separated
        return delete_id, message, relation, success 200
        if any problem in id relation_id raise 404, partenr raise 404,
        if any problem when update raise 422
        relation={
            1: "Father",
            2: "Mother",
            3: "wife",
            4: "husband",
            5: "child"
        }
        '''
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
        if name_person is None:
            abort(422)
        namePartenr = Person.query.filter_by(person_id=partenr).one_or_none()
        if namePartenr is None:
            abort(422)
        try:
            relations.person = person
            relations.partenr = partenr
            relations.relation = relation
            relations.update()
            message = ""
            if relation >= 5:
                message = name_person.name.format()+" became the " + \
                    RELATION_CONST[relation-1]+" of "+namePartenr.name.format()
            else:
                message = namePartenr.name.format()+" became the " +\
                    RELATION_CONST[relation-1]+" of "+name_person.name.format()
            return jsonify({
                "success": True,
                "persons": name_person.name.format(),
                "partenr": namePartenr.name.format(),
                "relation": message
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
            "description": "may be data missing"
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
            "description": "The server could not verify that you are " +
            "authorized to access the URL requested.You either supplied the " +
            "wrong credentials (e.g. a bad password),or your browser doesn't" +
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

    @app.errorhandler(AuthError)
    def handle_auth_error(exception):
        '''
    error handler for AuthError
        error handler is conform to general task above
        '''
        response = jsonify(exception.error)
        response.status_code = exception.status_code
        return response
    return app


app = create_app()

if __name__ == '__main__':
    app.run()
