import unittest


from app import db
from backend.admin.models import User
from backend.admin.tests.factories import UserFactory
from backend.test_config import BaseTestConfig


class TestAuthorizationModels(BaseTestConfig):
    """TestAuthorizationModels"""

    def setUp(self):
        db.create_all()
        db.session.expire_on_commit = False
        self.user_factory = UserFactory()
        self.user = User(
            full_name=self.user_factory.full_name,
            email=self.user_factory.email,
            password=self.user_factory.password)
        db.session.add(self.user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_adding_user(self):
        self.assertEqual(
            self.user.email,
            User.query.one().email,
            msg="Cannot create user"
        )


if __name__ == "__main__":
    unittest.main()
