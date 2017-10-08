import factory

from backend.admin.models import Admin
from backend.user.tests.factories import UserFactory


class AdminFactory(factory.Factory):
    """Factory for creating dummy users with Admin rights"""
    class Meta:
        model = Admin

    password = factory.LazyAttribute(lambda a: '{0}'.format("password"))
    user_id = factory.SubFactory(UserFactory)
