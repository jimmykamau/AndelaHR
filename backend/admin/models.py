from app import db


class User(db.Model):
    # Base user class
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    full_name = db.Column(db.String(255))

    # Representation of model (for Flask-JWT)
    def __repr__(self):
        return (str(self.id))
