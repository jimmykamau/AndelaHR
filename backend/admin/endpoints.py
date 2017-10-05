from flask import request
from flask_restful import Resource, abort
from werkzeug.security import generate_password_hash

from app import db
from backend.admin.models import User
from backend.admin.schemas import UserSchema


user_schema = UserSchema()


class UserRegistration(Resource):
    """Handle registration endpoints"""

    def get(self):
        pass

    def post(self):
        json_data = request.get_json()
        if not json_data:
            abort(400, message="Empty request")

        data, errors = user_schema.load(json_data)
        if errors:
            abort(422, message=errors)

        try:
            hash_password = generate_password_hash(data['password'])
            new_user = User(
                full_name=data['full_name'],
                email=data['email'],
                password=hash_password)
            db.session.add(new_user)
            db.session.commit()
            return {
                'message': "{} created successfully".format(data['full_name'])
            }, 201
        except Exception:
            abort(500, message="User not created due to internal server error")

    def put(self):
        pass

    def delete(self):
        pass
