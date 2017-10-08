from sqlalchemy.orm import backref

from app import db
from backend.user.models import User


class Task(db.Model):
    """Base Task class"""
    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    task_type = db.Column(db.Integer)


class TaskDetail(db.Model):
    """Task detail model"""
    __tablename__ = 'task_detail'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    task_id = db.Column(
        db.Integer, db.ForeignKey('task.id', ondelete='CASCADE'))
    date_due = db.Column(db.DateTime())

    user = db.relationship(
        User, backref=backref('task_detail', passive_deletes=True))
    task = db.relationship(
        Task, backref=backref('task_detail', passive_deletes=True))
