from flask import request
from flask_restful import Resource, abort

from app import db
from backend.task.models import Task, TaskDetail
from backend.task.schemas import TaskSchema, TaskDetailSchema


task_schema = TaskSchema()
task_detail_schema = TaskDetailSchema()


class TaskCategory(Resource):
    """Handle TaskCategory endpoints"""
    def post(self):
        json_data = request.get_json()
        if not json_data:
            abort(400, message="Empty request")

        data, errors = task_schema.load(json_data)
        if errors:
            abort(422, message=errors)

        try:
            new_task_category = Task(
                name=data['name'],
                description=data['description'],
                task_type=data['task_type'])
            db.session.add(new_task_category)
            db.session.commit()

        except Exception as e:
            abort(
                500, message="Task not created due to internal server error")
