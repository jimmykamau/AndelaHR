import unittest

from app import db
from backend.task.models import Task, TaskDetail
from backend.task.tests.factories import TaskFactory, TaskDetailFactory
from backend.test_config import BaseTestConfig
from backend.user.models import User


class TestTaskModel(BaseTestConfig):
    def setUp(self):
        db.create_all()
        db.session.expire_on_commit = False

        self.task_factory = TaskFactory()
        self.task = Task(
            name=self.task_factory.name,
            description=self.task_factory.description,
            task_type=self.task_factory.task_type)
        db.session.add(self.task)
        db.session.commit()

    def test_create_task(self):
        self.assertEqual(
            self.task_factory.name,
            Task.query.one().name,
            msg="Cannot add task to database")


class TestTaskDetailModel(BaseTestConfig):
    def setUp(self):
        db.create_all()
        db.session.expire_on_commit = False

        self.task_detail_factory = TaskDetailFactory()

        self.user = User(
            full_name=self.task_detail_factory.user_id.full_name,
            email=self.task_detail_factory.user_id.email)
        db.session.add(self.user)
        db.session.commit()

        self.task = Task(
            name=self.task_detail_factory.task_id.name,
            description=self.task_detail_factory.task_id.description,
            task_type=self.task_detail_factory.task_id.task_type)
        db.session.add(self.task)
        db.session.commit()

        self.task_detail = TaskDetail(
            user_id=self.user.id,
            task_id=self.task.id,
            date_due=self.task_detail_factory.date_due)
        db.session.add(self.task_detail)
        db.session.commit()

    def test_create_task_detail(self):
        self.assertEqual(
            self.task_detail_factory.date_due,
            TaskDetail.query.one().date_due,
            msg="Cannot add task detail to db")


if __name__ == "__main__":
    unittest.main()
