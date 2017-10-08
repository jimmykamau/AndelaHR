from sqlalchemy.orm import backref

from app import db
from backend.user.models import User


class Admin(db.Model):
    # Admin class
    __tablename__ = 'admin'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    password = db.Column(db.String(255))

    user = db.relationship(
        User, backref=backref('admin', passive_deletes=True))

    # Representation of model (for Flask-JWT)
    def __repr__(self):
        return (str(self.id))
