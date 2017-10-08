from datetime import datetime
from random import randint

import factory

from backend.user.tests.factories import UserFactory
from backend.task.models import Task, TaskDetail


class TaskFactory(factory.Factory):
    """Factory for creating dummy tasks"""
    class Meta:
        model = Task

    name = factory.Sequence(lambda n: "Task {0}".format(n))
    description = factory.Faker('sentence', nb_words=20)
    task_type = factory.LazyAttribute(lambda n: randint(1, 2))


class TaskDetailFactory(factory.Factory):
    class Meta:
        model = TaskDetail

    user_id = factory.SubFactory(UserFactory)
    task_id = factory.SubFactory(TaskFactory)
    date_due = factory.LazyFunction(datetime.now)
