import unittest

from app import db
from backend.admin.models import User, Admin
from backend.admin.tests.factories import AdminFactory
from backend.test_config import BaseTestConfig


class TestAuthorizationModels(BaseTestConfig):
    """TestAuthorizationModels"""

    def setUp(self):
        db.create_all()
        db.session.expire_on_commit = False

        self.admin_factory = AdminFactory()

        self.admin_user = User(
            full_name=self.admin_factory.user_id.full_name,
            email=self.admin_factory.user_id.email)
        db.session.add(self.admin_user)
        db.session.commit()

        self.admin_details = Admin(
            user_id=self.admin_user.id,
            password=self.admin_factory.password)
        db.session.add(self.admin_details)
        db.session.commit()

    def test_creating_admin(self):
        self.assertEqual(
            self.admin_factory.user_id.email,
            User.query.filter_by(id=Admin.query.one().user_id).one().email,
            msg="Cannot create admin user"
        )


if __name__ == "__main__":
    unittest.main()
