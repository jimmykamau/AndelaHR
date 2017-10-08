import unittest

from app import db
from backend.test_config import BaseTestConfig
from backend.user.models import User
from backend.user.tests.factories import UserFactory


class TestUserModels(BaseTestConfig):

    def setUp(self):
        db.create_all()
        db.session.expire_on_commit = False
        self.user_factory = UserFactory()
        self.user = User(
            full_name=self.user_factory.full_name,
            email=self.user_factory.email)
        db.session.add(self.user)
        db.session.commit()

    def test_creating_user(self):
        self.assertEqual(
            self.user_factory.email,
            User.query.one().email,
            msg="Cannot create user"
        )


if __name__ == "__main__":
    unittest.main()
