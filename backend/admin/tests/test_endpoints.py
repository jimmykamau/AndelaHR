import json
import unittest

from app import db
from backend.admin.models import Admin
# from backend.admin.tests.factories import AdminFactory
from backend.user.models import User
from backend.test_config import BaseTestConfig


class TestAuthorizationEndpoints(BaseTestConfig):
    """TestAuthorizationEndpoints"""
    def setUp(self):
        db.create_all()
        db.session.expire_on_commit = False

        self.create_and_login_admin()
        # self.admin_factory = AdminFactory()
        # self.admin_details = {
        #     'full_name': self.admin_factory.user_id.full_name,
        #     'email': self.admin_factory.user_id.email,
        #     'password': self.admin_factory.password
        # }

        # self.client.post(
        #     '/auth/register/',
        #     data=json.dumps(dict(self.admin_details)),
        #     content_type='application/json')

    def test_admin_creation(self):
        self.assertGreater(
            len(User.query.all()), 0,
            msg="Cannot create admin user via endpoint")
        self.assertGreater(
            len(Admin.query.all()), 0,
            msg="Cannot create admin via endpoint")

    def test_admin_login(self):
        # user_login_details = {
        #     'username': self.admin_details['email'],
        #     'password': self.admin_details['password']
        # }
        # user_login_response = self.client.post(
        #     '/auth/login',
        #     data=json.dumps(dict(user_login_details)),
        #     content_type='application/json')
        self.assertEqual(
            self.login_response.status_code, 200,
            msg="Login endpoint not working")
        self.assertTrue(
            self.login_response.json['access_token'],
            msg="Access token not returned")


if __name__ == "__main__":
    unittest.main()
