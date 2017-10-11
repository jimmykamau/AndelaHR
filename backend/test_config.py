import json
import flask_testing

from app import app, db
from backend.admin.tests.factories import AdminFactory


class BaseTestConfig(flask_testing.TestCase):
    """Base test setup"""
    def create_app(self):
        app.config['TESTING'] = True
        app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = False
        return app

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def create_and_login_admin(self):
        self.admin_factory = AdminFactory()
        self.admin_details = {
            'full_name': self.admin_factory.user_id.full_name,
            'email': self.admin_factory.user_id.email,
            'password': self.admin_factory.password
        }
        self.client.post(
            '/auth/register/',
            data=json.dumps(dict(self.admin_details)),
            content_type='application/json')
        print("here")

        user_login_details = {
            'username': self.admin_details['email'],
            'password': self.admin_details['password']
        }
        self.login_response = self.client.post(
            '/auth/login',
            data=json.dumps(dict(user_login_details)),
            content_type='application/json')

        print(self.login_response.data)
        self.user_token = json.loads(
            self.login_response.data.decode('utf-8', ['access_token']))
        self.auth_header = {
            'Authorization': 'JWT {}'.format(self.user_token)
        }
