import flask_testing

from app import app, db


class BaseTestConfig(flask_testing.TestCase):
    """Base test setup"""
    def create_app(self):
        app.config['TESTING'] = True
        app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = False
        return app

    def tearDown(self):
        db.session.remove()
        db.drop_all()
