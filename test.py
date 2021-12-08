import base64
import json
import pytest
from Lab_7 import app as fl_app
from Lab_7 import *
from json import *
import os
import tempfile

session = Session()


@pytest.fixture
def app():
    yield fl_app


@pytest.fixture
def client(app):
    return app.test_client()


class TestUser:
    def test_user_create(self, client):
        session.query(user).filter(user.username == "username7").delete()
        session.commit()

        temp = {
            "username": "username7",
            "firstName": "aaaaaaaaaa",
            "lastName": "aaaaaaaaaaa",
            "email": "maaaaaaaaaaaaaaaaaaaaaaax3@gmail.com",
            "password": "password",
            "phone": "0000",
            "userStatus": "admin"
        }

        temp = json.dumps(temp)

        response = client.post('http://localhost:5000/user',
                               headers={'Content-Type': 'application/json', 'Accept': 'application/json'},
                               data=temp)

        assert response.status_code == 200

    def test_get_users(self, client):
        response = client.get('http://localhost:5000/user',
                              headers={'Content-Type': 'application/json', 'Accept': 'application/json'})

        assert response.status_code == 200

    def test_duplicate_key(self, client):
        temp = dict(
            id=1,
            username='username',
            password='password'
        )
        response = client.post('http://localhost:5000/user', headers={'Content-Type': 'application/json'},
                               data=temp)

        assert response.status_code == 400

    def test_login(self, client):
        response = client.get("http://localhost:5000/user/login?username=username7&password=password",
                              headers={'Content-Type': 'application/json', 'Accept': 'application/json'})
        # TestUser.temp_token += response.data
        assert response.status_code == 200

    def test_login_failed(self, client):
        response = client.get("http://localhost:5000/user/login?username=username&password=password",
                              headers={'Content-Type': 'application/json', 'Accept': 'application/json'})
        assert response.status_code == 401

    def test_login_failed_2(self, client):
        response = client.get("http://localhost:5000/user/login",
                              headers={'Content-Type': 'application/json', 'Accept': 'application/json'})
        assert response.status_code == 401

    def test_login_failed_3(self, client):
        response = client.get("http://localhost:5000/user/login?username=username7&password=p",
                              headers={'Content-Type': 'application/json', 'Accept': 'application/json'})
        assert response.status_code == 401

    def test_logout(self, client):
        response = client.get("http://localhost:5000/user/logout")
        assert response.status_code == 200

    def test_delete_user(self, client):
        response = client.delete('http://localhost:5000/user/username7',
                                 headers={'Content-Type': 'application/json', 'Accept': 'application/json',
                                          'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzODkwOTYwMiwianRpIjoiNWM0NGRiOTItYzA3ZS00Mzk4LTgzNzQtMmRlZWI5ZGJlYTYwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJuYW1lNyIsIm5iZiI6MTYzODkwOTYwMiwiZXhwIjoxNjM5NTE0NDAyfQ.51icvc5bArgV27zVauQYWzPLAvpqizgREZUhNg4gkdE'
                                          })
        temp = {
            "username": "username7",
            "firstName": "aaaaaaaaaa",
            "lastName": "aaaaaaaaaaa",
            "email": "maaaaaaaaaaaaaaaaaaaaaaax3@gmail.com",
            "password": "password",
            "phone": "0000",
            "userStatus": "admin"
        }

        temp = json.dumps(temp)

        client.post('http://localhost:5000/user',
                    headers={'Content-Type': 'application/json', 'Accept': 'application/json',
                             'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzODkwOTYwMiwianRpIjoiNWM0NGRiOTItYzA3ZS00Mzk4LTgzNzQtMmRlZWI5ZGJlYTYwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJuYW1lNyIsIm5iZiI6MTYzODkwOTYwMiwiZXhwIjoxNjM5NTE0NDAyfQ.51icvc5bArgV27zVauQYWzPLAvpqizgREZUhNg4gkdE'},
                    data=temp)
        assert response.status_code == 200

    def test_delete_user_by_id_fail(self, client):
        response = client.delete('http://localhost:5000/user/username',
                                 headers={'Content-Type': 'application/json', 'Accept': 'application/json',
                                          'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzODkwOTYwMiwianRpIjoiNWM0NGRiOTItYzA3ZS00Mzk4LTgzNzQtMmRlZWI5ZGJlYTYwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJuYW1lNyIsIm5iZiI6MTYzODkwOTYwMiwiZXhwIjoxNjM5NTE0NDAyfQ.51icvc5bArgV27zVauQYWzPLAvpqizgREZUhNg4gkdE'
                                          })
        assert response.status_code == 500

    def test_get_user_by_id(self, client):
        response = client.get('http://localhost:5000/user/username7',
                              headers={'Content-Type': 'application/json', 'Accept': 'application/json',
                                       'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzODkwOTYwMiwianRpIjoiNWM0NGRiOTItYzA3ZS00Mzk4LTgzNzQtMmRlZWI5ZGJlYTYwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJuYW1lNyIsIm5iZiI6MTYzODkwOTYwMiwiZXhwIjoxNjM5NTE0NDAyfQ.51icvc5bArgV27zVauQYWzPLAvpqizgREZUhNg4gkdE'
                                       })
        assert response.status_code == 200

    def test_get_user_by_id_failed(self, client):
        response = client.get('http://localhost:5000/user/username',
                              headers={'Content-Type': 'application/json', 'Accept': 'application/json',
                                       'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzODkwOTYwMiwianRpIjoiNWM0NGRiOTItYzA3ZS00Mzk4LTgzNzQtMmRlZWI5ZGJlYTYwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJuYW1lNyIsIm5iZiI6MTYzODkwOTYwMiwiZXhwIjoxNjM5NTE0NDAyfQ.51icvc5bArgV27zVauQYWzPLAvpqizgREZUhNg4gkdE'
                                       })
        assert response.status_code == 500

    def test_upd_user_by_Id(self, client):
        temp = {
            "username": "username7",
            "firstName": "aaaaaaaaab",
            "lastName": "aaaaaaaaaaa",
            "email": "maaaaaaaaaaaaaaaaaaaaaaax3@gmail.com",
            "password": "password",
            "phone": "0000",
            "userStatus": "admin"
        }

        temp = json.dumps(temp)
        response = client.put('http://localhost:5000/user/username7',
                              headers={'Content-Type': 'application/json', 'Accept': 'application/json',
                                       'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzODkwOTYwMiwianRpIjoiNWM0NGRiOTItYzA3ZS00Mzk4LTgzNzQtMmRlZWI5ZGJlYTYwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJuYW1lNyIsIm5iZiI6MTYzODkwOTYwMiwiZXhwIjoxNjM5NTE0NDAyfQ.51icvc5bArgV27zVauQYWzPLAvpqizgREZUhNg4gkdE'
                                       }, data=temp)

        assert response.status_code == 200

    def test_upd_user_by_Id_failed(self, client):
        temp = {
            "username": "username7",
            "firstName": "aaaaaaaaaa",
            "lastName": "aaaaaaaaaaa",
            "email": "maaaaaaaaaaaaaaaaaaaaaaax3@gmail.com",
            "password": "password",
            "phone": "0000",
            "userStatus": "admin"
        }

        temp = json.dumps(temp)
        response = client.put('http://localhost:5000/user/username',
                              headers={'Content-Type': 'application/json', 'Accept': 'application/json',
                                       'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzODkwOTYwMiwianRpIjoiNWM0NGRiOTItYzA3ZS00Mzk4LTgzNzQtMmRlZWI5ZGJlYTYwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJuYW1lNyIsIm5iZiI6MTYzODkwOTYwMiwiZXhwIjoxNjM5NTE0NDAyfQ.51icvc5bArgV27zVauQYWzPLAvpqizgREZUhNg4gkdE'
                                       }, data=temp)

        assert response.status_code == 500


class TestStore:
    def test_store_create(self, client):
        temp = {
            "name": "aaaaa",
            "category": "bbbbbb",
            "goods": []
        }

        temp = json.dumps(temp)
        response = client.post('http://localhost:5000/store/store',
                               headers={'Content-Type': 'application/json', 'Accept': 'application/json',
                                        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzODk5NzI2NSwianRpIjoiNzcxNDBkMGYtMzc3Mi00MGQ0LTgzNDgtNTU1ZjMyZmU4Yjc0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJuYW1lMDAiLCJuYmYiOjE2Mzg5OTcyNjUsImV4cCI6MTYzOTYwMjA2NX0.c4sUO-HC_1tluS4JGJ-9Ee4s1l0QOF3Anr0UNS1k4-E'
                                        }, data=temp)

        assert response.status_code == 200

    def test_store_create_fail(self, client):
        temp = {
            "name": "aaaaa",
            "category": "bbbbbb",
            "goods": "cccc"
        }

        temp = json.dumps(temp)
        response = client.post('http://localhost:5000/store/store',
                               headers={'Content-Type': 'application/json', 'Accept': 'application/json',
                                        'Authorization': 'Bearer eyJeXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzODkwOTYwMiwianRpIjoiNWM0NGRiOTItYzA3ZS00Mzk4LTgzNzQtMmRlZWI5ZGJlYTYwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJuYW1lNyIsIm5iZiI6MTYzODkwOTYwMiwiZXhwIjoxNjM5NTE0NDAyfQ.51icvc5bArgV27zVauQYWzPLAvpqizgREZUhNg4gkdE'
                                        }, data=temp)

        assert response.status_code == 422

    def test_store_create_fail2(self, client):
        temp = {
            "name": "aaaaa",
            "category": "bbbbbb",
            "goods": "cccc"
        }

        temp = json.dumps(temp)
        response = client.post('http://localhost:5000/store/store',
                               headers={'Content-Type': 'application/json', 'Accept': 'application/json',
                                        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzODkxMjQ1NCwianRpIjoiM2JkNTI3NDUtM2Y0Ni00ZWNiLWI1ODEtMTJjZjY5ZTFiNWNmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJuYW1lMTEiLCJuYmYiOjE2Mzg5MTI0NTQsImV4cCI6MTYzOTUxNzI1NH0.ttsNMLC2_SybMqqvUzqPf_wAy0gk-t9m9Btzsqhn7Gc'
                                        }, data=temp)

        assert response.status_code == 401

    def test_good_create(self, client):
        temp = {
            "name": "string",
            "isAvailable": True,
            "photoUrls": ["string"],
            "status": "available"
        }

        temp = json.dumps(temp)
        response = client.post('http://localhost:5000/store/goods/2',
                               headers={'Content-Type': 'application/json', 'Accept': 'application/json',
                                        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzODk5NzI2NSwianRpIjoiNzcxNDBkMGYtMzc3Mi00MGQ0LTgzNDgtNTU1ZjMyZmU4Yjc0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJuYW1lMDAiLCJuYmYiOjE2Mzg5OTcyNjUsImV4cCI6MTYzOTYwMjA2NX0.c4sUO-HC_1tluS4JGJ-9Ee4s1l0QOF3Anr0UNS1k4-E'
                                        }, data=temp)

        assert response.status_code == 200

    def test_good_create_fail(self, client):
        temp = {
            "name": "string",
            "isAvailable": True,
            "photoUrls": ["string"],
            "status": "available"
        }

        temp = json.dumps(temp)
        response = client.post('http://localhost:5000/store/goods/2',
                               headers={'Content-Type': 'application/json', 'Accept': 'application/json',
                                        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzODkxMjQ1NCwianRpIjoiM2JkNTI3NDUtM2Y0Ni00ZWNiLWI1ODEtMTJjZjY5ZTFiNWNmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJuYW1lMTEiLCJuYmYiOjE2Mzg5MTI0NTQsImV4cCI6MTYzOTUxNzI1NH0.ttsNMLC2_SybMqqvUzqPf_wAy0gk-t9m9Btzsqhn7Gc'
                                        }, data=temp)

        assert response.status_code == 401

    def test_get_goods(self, client):
        response = client.get('http://localhost:5000/store/goods/1',
                              headers={'Content-Type': 'application/json', 'Accept': 'application/json',
                                       'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzODk5NzI2NSwianRpIjoiNzcxNDBkMGYtMzc3Mi00MGQ0LTgzNDgtNTU1ZjMyZmU4Yjc0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJuYW1lMDAiLCJuYmYiOjE2Mzg5OTcyNjUsImV4cCI6MTYzOTYwMjA2NX0.c4sUO-HC_1tluS4JGJ-9Ee4s1l0QOF3Anr0UNS1k4-E'
                                       })
        assert response.status_code == 200

    def test_order_create(self, client):
        temp = {
            "goodsId": "1",
            "status": "123",
            "complete": True,
            "userId": "7"
        }

        temp = json.dumps(temp)
        response = client.post('http://localhost:5000/store/order',
                               headers={'Content-Type': 'application/json', 'Accept': 'application/json',
                                        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzODk5NzI2NSwianRpIjoiNzcxNDBkMGYtMzc3Mi00MGQ0LTgzNDgtNTU1ZjMyZmU4Yjc0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJuYW1lMDAiLCJuYmYiOjE2Mzg5OTcyNjUsImV4cCI6MTYzOTYwMjA2NX0.c4sUO-HC_1tluS4JGJ-9Ee4s1l0QOF3Anr0UNS1k4-E'
                                        }, data=temp)

        assert response.status_code == 200

    def test_order_create_fail(self, client):
        temp = {
            "goodsId": "1",
            "status": "1",
            "complete": "false"
        }

        temp = json.dumps(temp)
        response = client.put('http://localhost:5000/store/order',
                              headers={'Content-Type': 'application/json', 'Accept': 'application/json',
                                       'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzODkwOTYwMiwianRpIjoiNWM0NGRiOTItYzA3ZS00Mzk4LTgzNzQtMmRlZWI5ZGJlYTYwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJuYW1lNyIsIm5iZiI6MTYzODkwOTYwMiwiZXhwIjoxNjM5NTE0NDAyfQ.51icvc5bArgV27zVauQYWzPLAvpqizgREZUhNg4gkdE'
                                       }, data=temp)

        assert response.status_code == 405

    def test_delete_order_by_id(self, client):
        response = client.delete('http://localhost:5000/store/order/999',
                                 headers={'Content-Type': 'application/json', 'Accept': 'application/json',
                                          'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzODk5NzI2NSwianRpIjoiNzcxNDBkMGYtMzc3Mi00MGQ0LTgzNDgtNTU1ZjMyZmU4Yjc0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJuYW1lMDAiLCJuYmYiOjE2Mzg5OTcyNjUsImV4cCI6MTYzOTYwMjA2NX0.c4sUO-HC_1tluS4JGJ-9Ee4s1l0QOF3Anr0UNS1k4-E'
                                          })
        assert response.status_code == 500

    def test_delete_order_by_id_fail(self, client):
        response = client.delete('http://localhost:5000/store/order/1',
                                 headers={'Content-Type': 'application/json', 'Accept': 'application/json',
                                          'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzODkwOTYwMiwianRpIjoiNWM0NGRiOTItYzA3ZS00Mzk4LTgzNzQtMmRlZWI5ZGJlYTYwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJuYW1lNyIsIm5iZiI6MTYzODkwOTYwMiwiZXhwIjoxNjM5NTE0NDAyfQ.51icvc5bArgV27zVauQYWzPLAvpqizgREZUhNg4gkdE'
                                          })
        assert response.status_code == 401


class TestGoods:
    def test_get_goods(self, client):
        response = client.get('http://localhost:5000/goods/1',
                              headers={'Content-Type': 'application/json', 'Accept': 'application/json',
                                       'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzODk5NzI2NSwianRpIjoiNzcxNDBkMGYtMzc3Mi00MGQ0LTgzNDgtNTU1ZjMyZmU4Yjc0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJuYW1lMDAiLCJuYmYiOjE2Mzg5OTcyNjUsImV4cCI6MTYzOTYwMjA2NX0.c4sUO-HC_1tluS4JGJ-9Ee4s1l0QOF3Anr0UNS1k4-E'
                                       })
        assert response.status_code == 200

    def test_update_goods(self, client):
        temp = {
            "name": "string",
            "isAvailable": True,
            "photoUrls": ["string"],
            "status": "available"
        }

        temp = json.dumps(temp)
        response = client.put('http://localhost:5000/goods/string',
                              headers={'Content-Type': 'application/json', 'Accept': 'application/json',
                                       'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzODk5NzI2NSwianRpIjoiNzcxNDBkMGYtMzc3Mi00MGQ0LTgzNDgtNTU1ZjMyZmU4Yjc0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJuYW1lMDAiLCJuYmYiOjE2Mzg5OTcyNjUsImV4cCI6MTYzOTYwMjA2NX0.c4sUO-HC_1tluS4JGJ-9Ee4s1l0QOF3Anr0UNS1k4-E'
                                       }, data=temp)
        assert response.status_code == 200

    def test_update_goods_fail(self, client):
        temp = {
            "name": "string",
            "isAvailable": True,
            "photoUrls": ["string"],
            "status": "available"
        }

        temp = json.dumps(temp)
        response = client.put('http://localhost:5000/goods/string',
                              headers={'Content-Type': 'application/json', 'Accept': 'application/json',
                                       'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzODkwOTYwMiwianRpIjoiNWM0NGRiOTItYzA3ZS00Mzk4LTgzNzQtMmRlZWI5ZGJlYTYwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJuYW1lNyIsIm5iZiI6MTYzODkwOTYwMiwiZXhwIjoxNjM5NTE0NDAyfQ.51icvc5bArgV27zVauQYWzPLAvpqizgREZUhNg4gkdE'
                                       }, data=temp)
        assert response.status_code == 401

    def test_update_goods_fail_2(self, client):
        temp = {
            "name": "string",
            "isAvailable": True,
            "photoUrls": ["string"],
            "status": "available"
        }

        temp = json.dumps(temp)
        response = client.put('http://localhost:5000/goods/sing',
                              headers={'Content-Type': 'application/json', 'Accept': 'application/json',
                                       'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzODk5NzI2NSwianRpIjoiNzcxNDBkMGYtMzc3Mi00MGQ0LTgzNDgtNTU1ZjMyZmU4Yjc0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJuYW1lMDAiLCJuYmYiOjE2Mzg5OTcyNjUsImV4cCI6MTYzOTYwMjA2NX0.c4sUO-HC_1tluS4JGJ-9Ee4s1l0QOF3Anr0UNS1k4-E'
                                       }, data=temp)
        assert response.status_code == 401

    def test_update_goods_id(self, client):
        temp = {
            "name": "string",
            "isAvailable": True,
            "photoUrls": ["string"],
            "status": "available"
        }

        temp = json.dumps(temp)
        response = client.put('http://localhost:5000/goods/1',
                              headers={'Content-Type': 'application/json', 'Accept': 'application/json',
                                       'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzODk5NzI2NSwianRpIjoiNzcxNDBkMGYtMzc3Mi00MGQ0LTgzNDgtNTU1ZjMyZmU4Yjc0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJuYW1lMDAiLCJuYmYiOjE2Mzg5OTcyNjUsImV4cCI6MTYzOTYwMjA2NX0.c4sUO-HC_1tluS4JGJ-9Ee4s1l0QOF3Anr0UNS1k4-E'
                                       }, data=temp)
        assert response.status_code == 200

    def test_update_goods_fail_id(self, client):
        temp = {
            "name": "string",
            "isAvailable": True,
            "photoUrls": ["string"],
            "status": "available"
        }

        temp = json.dumps(temp)
        response = client.put('http://localhost:5000/goods/1',
                              headers={'Content-Type': 'application/json', 'Accept': 'application/json',
                                       'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzODkwOTYwMiwianRpIjoiNWM0NGRiOTItYzA3ZS00Mzk4LTgzNzQtMmRlZWI5ZGJlYTYwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJuYW1lNyIsIm5iZiI6MTYzODkwOTYwMiwiZXhwIjoxNjM5NTE0NDAyfQ.51icvc5bArgV27zVauQYWzPLAvpqizgREZUhNg4gkdE'
                                       }, data=temp)
        assert response.status_code == 401

    def test_update_goods_id_fail_2(self, client):
        temp = {
            "name": "string",
            "isAvailable": True,
            "photoUrls": ["string"],
            "status": "available"
        }

        temp = json.dumps(temp)
        response = client.put('http://localhost:5000/goods/999',
                              headers={'Content-Type': 'application/json', 'Accept': 'application/json',
                                       'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzODk5NzI2NSwianRpIjoiNzcxNDBkMGYtMzc3Mi00MGQ0LTgzNDgtNTU1ZjMyZmU4Yjc0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJuYW1lMDAiLCJuYmYiOjE2Mzg5OTcyNjUsImV4cCI6MTYzOTYwMjA2NX0.c4sUO-HC_1tluS4JGJ-9Ee4s1l0QOF3Anr0UNS1k4-E'
                                       }, data=temp)
        assert response.status_code == 401

    def test_get_goods_by_status(self, client):
        response = client.get('http://localhost:5000/goods/findByStatus?status=available',
                              headers={'Content-Type': 'application/json', 'Accept': 'application/json',
                                       'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzODk5NzI2NSwianRpIjoiNzcxNDBkMGYtMzc3Mi00MGQ0LTgzNDgtNTU1ZjMyZmU4Yjc0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJuYW1lMDAiLCJuYmYiOjE2Mzg5OTcyNjUsImV4cCI6MTYzOTYwMjA2NX0.c4sUO-HC_1tluS4JGJ-9Ee4s1l0QOF3Anr0UNS1k4-E'
                                       })
        assert response.status_code == 200

    def test_delete_goods_by_id(self, client):
        response = client.delete('http://localhost:5000/goods/9999',
                              headers={'Content-Type': 'application/json', 'Accept': 'application/json',
                                       'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzODk5NzI2NSwianRpIjoiNzcxNDBkMGYtMzc3Mi00MGQ0LTgzNDgtNTU1ZjMyZmU4Yjc0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJuYW1lMDAiLCJuYmYiOjE2Mzg5OTcyNjUsImV4cCI6MTYzOTYwMjA2NX0.c4sUO-HC_1tluS4JGJ-9Ee4s1l0QOF3Anr0UNS1k4-E'
                                       })
        assert response.status_code == 500
