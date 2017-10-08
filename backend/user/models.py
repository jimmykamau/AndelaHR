from app import db


class User(db.Model):
    # Base user class
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    full_name = db.Column(db.String(255))
