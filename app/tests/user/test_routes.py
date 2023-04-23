import pytest
import unittest
from app.app import create_app
from app.extensions.database.models import User
from flask_login import current_user, login_user

# class TestUserRoutes(unittest.TestCase):
#     def setUp(self):
#         self.app = create_app()
#         self.client = self.app.test_client()

#     def test_index_success(self):
#         response = self.client.get('/')
#         self.assertTrue(response.status_code == 200)
#         self.assertTrue(b'Welcome to SetBox!' in response.data)

#     def test_login_success(self):
#         response = self.client.get('/login')
#         assert response.status_code == 200

#     def test_register_success(self):
#         response = self.client.get('/register')
#         assert response.status_code == 200

# def test_register_works(self):
#     with self.client:
#         response = self.client.post('/register', data={
#             'email': 'test_registering@setbox.de',
#             'password': 'test_password',
#             'password_confirmation': 'test_password',
#             'fname': 'Testy'
#         }, follow_redirects=True)
#         # not working
#         assert current_user.is_authenticated
#         assert response.status_code == 200
#         assert User.query.filter_by(email='test_registering@setbox.de').first() is not None

#     def test_login_works(self):
#         user = User(
#             email='test_logingin@setbox.de',
#             first_name='Testy'
#         )
#         user.set_password('test_password')
#         with self.client:
#             response = self.client.post('/login', data={
#                 'email': 'test_logingin@setbox.de',
#                 'password': 'test_password'
#             }, follow_redirects=True)
#             # not working
#             assert current_user.is_authenticated
#             assert response.status_code == 200

#     def test_logout_works(self):
#         user = User(
#             email='test_logingout@setbox.de',
#             first_name='Testy'
#         )
#         user.set_password('test_password')
#         login_user(user)
#         #user.is_authenticated = True
#         with self.client:
#             response = self.client.get('/logout', follow_redirects=True)
#             assert not current_user.is_authenticated
#             assert response.status_code == 200
