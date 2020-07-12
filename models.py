from sqlalchemy import Column, String, create_engine, Integer, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
import json
import os
# from flask_migrate import Migrate


database_path = os.environ['DATABASE_URL']
db = SQLAlchemy()
'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    # migrate = Migrate(app, db)
    db.create_all()


'''
Person
Have name, gender, day_of_birth, day_of_death, notes, address,
   nickname and status
'''


class Person(db.Model):
    __tablename__ = 'Persons'
    person_id = Column(Integer, primary_key=True)
    name = Column(String)
    gender = Column(String)
    day_of_birth = Column(Integer)
    day_of_death = Column(Integer)
    notes = Column(String)
    address = Column(String)
    nickname = Column(String)
    status= Column(String)

    def __init__(self, name, gender, day_of_birth, day_of_death, notes, address,
    nickname, status):
        self.name = name
        self.gender = gender
        self.day_of_birth = day_of_birth
        self.day_of_death = day_of_death
        self.notes = notes
        self.address = address
        self.nickname = nickname
        self.status = status
    def insert(self):
        db.session.add(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def short(self):
        return{
            'person_id': self.person_id,
            'name': self.name
        }
    def shortName(self):
        return{
        'name': self.name
        } 
    def format(self):
        return {
            'person_id': self.person_id,
            'name': self.name,
            'gender': self.gender,
            'day_of_birth': self.day_of_birth,
            'day_of_death': self.day_of_death,
            'notes': self.notes,
            'address': self.address,
            'nickname': self.nickname,
            'status': self.status
        }

class Relations(db.Model):
    __tablename__ = 'Relations'
    relation_id = Column(Integer, primary_key=True)
    person = Column(Integer, ForeignKey('Persons.person_id'))
    partenr = Column(Integer, ForeignKey('Persons.person_id'))
    relation = Column(Integer)
    
    def __init__(self, partenr, relation, person):
        self.person = person
        self.partenr = partenr
        self.relation = relation
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def format(self):
        return {
            'relation_id': self.relation_id,
            'partenr': self.partenr,
            'relation': self.relation,
            "person": self.person
        }
