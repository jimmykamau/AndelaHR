import factory

from backend.user.models import User


class UserFactory(factory.Factory):
    """Factory for creating dummy users"""
    class Meta:
        model = User

    email = factory.LazyAttribute(
        lambda a: '{0}@domain.com'.format(
            a.full_name.replace(' ', '')).lower())
    full_name = factory.Faker('name')
