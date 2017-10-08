from flask import request
from flask_restful import Resource, abort

from app import db
from backend.user.models import User
from backend.user.schemas import UserSchema


user_schema = UserSchema()


class UserCreation(Resource):
    """Handle user creation endpoints"""
    def post(self):
        json_data = request.get_json()
        if not json_data:
            abort(400, message="Empty request")

        data, errors = user_schema.load(json_data)
        if errors:
            abort(422, message=errors)

        try:
            new_user = User(
                full_name=data['full_name'],
                email=data['email'])
            db.session.add(new_user)
            db.session.commit()
            return {
                'message': "{} created successfully".format(data['full_name'])
            }, 201
        except Exception:
            abort(500, message="User not created due to internal server error")
