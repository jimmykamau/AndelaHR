import json
import unittest

from app import db
from backend.task.tests.factories import TaskFactory, TaskDetailFactory
from backend.task.models import Task, TaskDetail
from backend.test_config import BaseTestConfig


class TestTaskEndpoints(BaseTestConfig):
    """TestTaskEndpoints"""
    def setUp(self):
        db.create_all()
        db.session.expire_on_commit = False

        self.task_factory = TaskFactory()
        self.task_details = {
            'name': self.task_factory.name,
            'description': self.task_factory.description,
            'task_type': self.task_factory.task_type
        }

        self.client.post(
            '/task/',
            data=json.dumps(dict(self.task_details)),
            content_type='application/json')

    def test_task_category_creation(self):
        self.assertGreater(
            len(Task.query.all()), 0,
            msg="Cannot create task from endpoint")


class TestTaskDetailEndpoints(BaseTestConfig):
    def setUp(self):
        db.create_all()
        db.session.expire_on_commit = False

        self.task_detail_factory = TaskDetailFactory()
        self.task_detail_contents = {
            'user_id': self.task_detail_factory.user_id.id,
            'task_id': self.task_detail_factory.task_id.id,
            'date_due': str(self.task_detail_factory.date_due)
        }

        self.client.post(
            '/task/assign/',
            data=json.dumps(dict(self.task_detail_contents)),
            content_type='application/json')

    def test_creation(self):
        self.assertGreater(
            len(TaskDetail.query.all()), 0,
            msg="Cannot assign task to candidate")


if __name__ == "__main__":
    unittest.main()
