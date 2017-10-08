import json
import unittest

from app import db
from backend.user.models import User
from backend.user.tests.factories import UserFactory
from backend.test_config import BaseTestConfig


class TestUserEndpoints(BaseTestConfig):

    def setUp(self):
        db.create_all()
        db.session.expire_on_commit = False

        self.user_factory = UserFactory()
        self.user_details = {
            'full_name': self.user_factory.full_name,
            'email': self.user_factory.email
        }

        self.user_creation_response = self.client.post(
            '/user/',
            data=json.dumps(dict(self.user_details)),
            content_type='application/json')

    def test_user_creation(self):
        self.assertEqual(
            201,
            self.user_creation_response.status_code,
            msg="Cannot create user via endpoint")

        self.assertEqual(
            self.user_details['email'],
            User.query.one().email,
            msg="User not added to database")


if __name__ == "__main__":
    unittest.main()
