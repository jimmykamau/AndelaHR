import json
import unittest

from app import db
from backend.admin.tests.factories import UserFactory
from backend.admin.models import User
from backend.test_config import BaseTestConfig


class TestAuthorizationEndpoints(BaseTestConfig):
    """TestAuthorizationEndpoints"""
    def setUp(self):
        db.create_all()
        db.session.expire_on_commit = False
        self.user_factory = UserFactory()
        self.user_details = {
            'full_name': self.user_factory.full_name,
            'email': self.user_factory.email,
            'password': self.user_factory.password
        }

        self.user_creation_response = self.client.post(
            '/auth/register/',
            data=json.dumps(dict(self.user_details)),
            content_type='application/json')

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_user_registration(self):
        self.assertEqual(
            201,
            self.user_creation_response.status_code,
            msg="Cannot create user via endpoint")

        self.assertEqual(
            self.user_details['email'],
            User.query.one().email,
            msg="User not added to database")

    def test_user_login(self):
        user_login_details = {
            'username': self.user_details['email'],
            'password': self.user_details['password']
        }
        user_login_response = self.client.post(
            '/auth/login',
            data=json.dumps(dict(user_login_details)),
            content_type='application/json')
        self.assertEqual(
            user_login_response.status_code, 200,
            msg="Login endpoint not working")
        self.assertTrue(
            user_login_response.json['access_token'],
            msg="Access token not returned")


if __name__ == "__main__":
    unittest.main()
