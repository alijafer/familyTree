import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Person, Relations
from typing import Final
from auth import AuthError, requires_auth


version  : Final = "v1"
token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5aWnZlbTNiMDVxR2hra0t1MUJldiJ9.eyJpc3MiOiJodHRwczovL2FsaWRldi5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWViZmEyMmI4YjIzOWQwYmZlNmRlMGY4IiwiYXVkIjoiZmFtaWx5VHJlZUFwaSIsImlhdCI6MTU5NDUzNTcwMSwiZXhwIjoxNTk0NTQyOTAxLCJhenAiOiJrTUNyVHJpUDNzYnhINXZQaWR4eUhQQmxIbFFOZUMyQyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOnBhcnRlbnIiLCJkZWxldGU6cGVyc29uIiwiZ2V0OnBhcnRlbnIiLCJnZXQ6cGVyc29uIiwicGF0Y2g6cGFydGVuciIsInBhdGNoOnBlcnNvbiIsInBvc3Q6cGFydGVuciIsInBvc3Q6cGVyc29uIl19.lmhf-5c3Qoy0HvaaIcHEVkJoOBf8g3MZaGvXYuZVrDkJCfbT6PYIlBp824y85s_p5arGLGpBKOA3EGzksy0aatOMsbo7l3-u-HfMtf4s53x31WIx4sLFPMw5uvI9FvQ7qn2I6nKuH7j1P4YoiWmnNejsySShcOma3rYnr3vTHm8juNCWAXkwmg1ZlgQxYAXKTob2QMJSOUeDXFBKnBZbDlmtlMrGOz_7HbFXWB_F2P8zlXnWvGdhyqRVmny2hTRXRLCVJVkqZ1ClLS46pfmiLDf14k2ui93XURCakRk85EMgYZiAaKmHQMdMbsU8ObM1vEHxttsr8mEE0b8Af1l86w"
headers1 = {'Content-Type': 'application/json', 'Authorization': 'Bearer '+ token}
class familyTreeTestCase(unittest.TestCase):
    """This class represents the trivia test case"""
    

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "famliytree_test1"
        self.username = 'postgres'
        self.password = '1'
        self.database_path = "postgresql://{}:{}@{}/{}".format(
            self.username, self.password, 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        self.new_person1 = {
            "address": "ahsaa",
            "day_of_birth": 1994,
            "day_of_death": 2050,
            "gender": "m",
            "name": "ali",
            "nickname": "bo jafer",
            "notes": "test",
            "status": "live"
        }
        self.new_person2 = {
            "address": "ahsaa",
            "day_of_birth": 1998,
            "day_of_death": 2050,
            "gender": "f",
            "name": "alaa",
            "nickname": "um hassan",
            "notes": "test",
            "status": "live"
        }
        self.new_person_empty = {
            "address": "",
            "day_of_birth": None,
            "day_of_death": None,
            "gender": "",
            "name": "",
            "nickname": "",
            "notes": "",
            "status": ""
        }
        self.new_relation = {
            "partenr": 2,
            "person": 1,
            "relation": 3
        }
        self.new_relation_empty = {
            "partenr": None,
            "person": None,
            "relation": None
        }
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
        
    def tearDown(self):
        """Executed after reach test"""
        pass
    
    def test_get_all_person(self):
        '''
        Test to get all person
        return 'success': True, "persons": "persons"
        :pass
        '''
        # code for test GET methods  that send Get reaquset to /example
        res = self.client().get("/"+version+"/person", headers=headers1)
        # featch the GET response
        data = json.loads(res.data)
        # confirm the status response code is 200 is mean Ok
        self.assertEqual(res.status_code, 200)
        # confirm the respones pass success is true
        self.assertEqual(data['success'], True)
        # confirm the respones pass the persons
        self.assertTrue(data['persons'])
        # confirm the respones get 3 persons
        self.assertEqual(len(data['persons']), 3)

    def test_get_all_person_without_token(self):
        '''
        Test to get all person without token
        return 'success': False, 
        :pass
        '''
        # code for test GET methods  that send Get reaquset to /example
        res = self.client().get("/"+version+"/person")
        # featch the GET response
        #data = json.loads(res.data)
        # confirm the status response code is 200 is mean Ok
        self.assertEqual(res.status_code, 401)
        #print(data)

    def test_get_paginate_persons(self):
        '''
        Test to get 3 persons
        return 'success': True, get maximum 3 persons
        :pass
        '''
        # code for test GET methods  that send Get reaquset to /example
        res = self.client().get('/'+version+'/person', headers=headers1)
        # featch the GET response
        data = json.loads(res.data)
        # confirm the status response code is 200 is mean Ok
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['persons'])
        # test and confirm the response has 3 persons
        self.assertEqual(len(data['persons']), 3)


    def test_error_paginate_persons(self):
        '''
        Test the unreasonable number set in pages
        return 'success': False, 404, and resource not found
        :pass
        '''
        # code for test GET methods  that send Get reaquset to /example
        res = self.client().get('/'+version+'/person?page=10000000', headers=headers1)
        # featch the GET response
        data = json.loads(res.data)
        # confirm the status response code is 404 is mean resource not found
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        # confirm response has element equal "message": "resource not found"
        self.assertEqual(data['message'], 'resource not found')


    def test_create_new_Person(self):
        '''
        Test insert person with data in db
        :pass
        '''
        # code for test POST methods  that send POST reaquset to /example
        res = self.client().post('/'+version+'/person', json=self.new_person1, headers=headers1)
        # featch the post response
        data = json.loads(res.data)
        # confirm the status response code is 200 is mean Ok
        self.assertEqual(res.status_code, 200)
        self.assertIsNotNone(data['persons'])

    def test_create_new_Person_without_token(self):
        '''
        Test insert person with data in db
        :pass
        '''
        # code for test POST methods  that send POST reaquset to /example
        res = self.client().post('/'+version+'/person', json=self.new_person1)
        # featch the post response
        # data = json.loads(res.data)
        # confirm the status response code is 200 is mean Ok
        self.assertEqual(res.status_code, 401)

    def test_404_if_person_creation_no_data(self):
        '''
        Test insert person without data in db
        :pass
        '''
        # code for test POST methods  that send POST reaquset to /example
        res = self.client().post('/'+version+'/person', json=self.new_person_empty, headers=headers1)
        # featch the post response
        data = json.loads(res.data)
        # confirm the status response code is 422 is mean unprocessable
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')


    def test_create_new_partenr(self):
        '''
        Test insert partenr with data in db
        :pass
        '''
        # code for test POST methods  that send POST reaquset to /example
        res = self.client().post('/'+version+'/partenr', json=self.new_relation, headers=headers1)
        # featch the post response
        data = json.loads(res.data)
        # confirm the status response code is 200 is mean Ok
        self.assertEqual(res.status_code, 200)
        self.assertIsNotNone(data['person'])
    def test_create_new_partenr_without_token(self):
        '''
        Test insert partenr with data in db
        :pass
        '''
        # code for test POST methods  that send POST reaquset to /example
        res = self.client().post('/'+version+'/partenr', json=self.new_relation)
        # featch the post response
        # data = json.loads(res.data)
        # confirm the status response code is 200 is mean Ok
        self.assertEqual(res.status_code, 401)

    def test_404_if_partenr_creation_no_data(self):
        '''
        Test insert partenr without data in db
        :pass
        '''
        # code for test POST methods  that send POST reaquset to /example
        res = self.client().post('/'+version+'/partenr', json=self.new_relation_empty, headers=headers1)
        # featch the post response
        data = json.loads(res.data)
        # confirm the status response code is 422 is mean unprocessable
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_sucsse_update_person(self):
        '''
        Test update partenr with data in db
        :pass
        '''
        # code for test POST methods  that send POST reaquset to /example
        res = self.client().patch('/'+version+'/person/1', json=self.new_person2, headers=headers1)
        # featch the post response
        data = json.loads(res.data)
        # confirm the status response code is 200 is mean Ok
        self.assertEqual(res.status_code, 200)
        self.assertIsNotNone(data['persons'])

    def test_sucsse_update_person_without_token(self):
        '''
        Test update partenr with data in db
        :pass
        '''
        # code for test POST methods  that send POST reaquset to /example
        res = self.client().patch('/'+version+'/person/1', json=self.new_person2)
        # featch the post response
        # data = json.loads(res.data)
        # confirm the status response code is 200 is mean Ok
        self.assertEqual(res.status_code, 401)

    def test_unsucsse_update_person(self):
        '''
        Test update partenr with data in db 
        :pass
        '''
        # code for test POST methods  that send POST reaquset to /example
        res = self.client().patch('/'+version+'/person/1', json=self.new_person_empty, headers=headers1)
        # featch the post response
        data = json.loads(res.data)
        # confirm the status response code is 200 is mean Ok
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "unprocessable")

    def test_sucsse_update_partenr(self):
        '''
        Test update partenr with data in db
        :pass
        '''
        # code for test POST methods  that send POST reaquset to /example
        res = self.client().patch('/'+version+'/partenr/1', headers=headers1 , json=self.new_relation)
        # featch the post response
        data = json.loads(res.data)
        # confirm the status response code is 200 is mean Ok
        self.assertEqual(res.status_code, 200)
        self.assertIsNotNone(data['persons'])
    def test_sucsse_update_partenr_without_token(self):
        '''
        Test update partenr with data in db
        :pass
        '''
        # code for test POST methods  that send POST reaquset to /example
        res = self.client().patch('/'+version+'/partenr/1', json=self.new_relation)
        # featch the post response
        # data = json.loads(res.data)
        # confirm the status response code is 401 is mean Ok
        self.assertEqual(res.status_code, 401)


    def test_unsucsse_update_partenr(self):
        '''
        Test update partenr with data in db 
        :pass
        '''
        # code for test POST methods  that send POST reaquset to /example
        res = self.client().patch('/'+version+'/partenr/1', json=self.new_relation_empty, headers=headers1)
        # featch the post response
        data = json.loads(res.data)
        # confirm the status response code is 200 is mean Ok
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "unprocessable")
    
    def test_sucsse_delete_person(self):
        '''
        Test the delete the person exit in db
        :pass
        '''
        '''
        code for test DELETE methods  that send DELETE
        reaquset to /example/<int:id>
        '''
        res = self.client().delete('/'+version+'/person/9', headers=headers1)
        # featch the delete response
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['message'])
        self.assertTrue(data['delete_id'])

    def test_delete_person_without_token(self):
        '''
        Test the delete the person exit in db
        :pass
        '''
        '''
        code for test DELETE methods  that send DELETE
        reaquset to /example/<int:id>
        '''
        res = self.client().delete('/'+version+'/person/9')
        # featch the delete response
        # data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)

    def test_delete_person_not_exit(self):
        '''
        Test the delete the person not exit in db
        becesed cannot delete record not exit in db
        :pass
        '''
        '''
        code for test DELETE methods  that send DELETE
        reaquset to /example/<int:id>
        '''
        res = self.client().delete('/'+version+'/person/62334', headers=headers1)
        # featch the delete response
        data = json.loads(res.data)
        # confirm the status response code is 422 is mean unprocessable
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "resource not found")
    def test_sucsse_delete_partenr(self):
        '''
        Test the delete the partenr exit in db
        :pass
        '''
        '''
        code for test DELETE methods  that send DELETE
        reaquset to /example/<int:id>
        '''
        res = self.client().delete('/'+version+'/partenr/6', headers=headers1)
        # featch the delete response
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['message'])
        self.assertTrue(data['delete_id'])

    def test_delete_partenr_not_exit(self):
        '''
        Test the delete the partenr not exit in db
        becesed cannot delete record not exit in db
        :pass
        '''
        '''
        code for test DELETE methods  that send DELETE
        reaquset to /example/<int:id>
        '''
        res = self.client().delete('/'+version+'/partenr/62334', headers=headers1)
        # featch the delete response
        data = json.loads(res.data)
        # confirm the status response code is 422 is mean unprocessable
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "resource not found")
    def test_delete_partenr_without_token(self):
        '''
        Test the delete the partenr not exit in db
        becesed cannot delete record not exit in db
        :pass
        '''
        '''
        code for test DELETE methods  that send DELETE
        reaquset to /example/<int:id>
        '''
        res = self.client().delete('/'+version+'/partenr/62334')
        # featch the delete response
        # data = json.loads(res.data)
        # confirm the status response code is 422 is mean unprocessable
        self.assertEqual(res.status_code, 401)
    def test_persons_get_partenr(self):  
        '''
        Test to get all person
        return 'success': True, "persons": "persons"
        :pass
        '''
        # code for test GET methods  that send Get reaquset to /example
        res = self.client().get("/"+version+"/partenr/2")
        # featch the GET response
        data = json.loads(res.data)
        # confirm the status response code is 200 is mean Ok
        self.assertEqual(res.status_code, 200)
        # confirm the respones pass success is true
        self.assertEqual(data['success'], True)
        # confirm the respones pass the persons
        self.assertTrue(data['data'])
    def test_error_persons_get_partenr(self):  
        '''
        Test to get all person
        return 'success': True, "persons": "persons"
        :pass
        '''
        # code for test GET methods  that send Get reaquset to /example
        res = self.client().get("/"+version+"/partenr/1")
        # featch the GET response
        data = json.loads(res.data)
        # confirm the status response code is 422 is mean Ok
        self.assertEqual(res.status_code, 422)



if __name__ == '__main__':
    unittest.main()