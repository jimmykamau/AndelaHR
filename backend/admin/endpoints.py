from flask import request
from flask_restful import Resource, abort
from werkzeug.security import generate_password_hash

from app import db
from backend.admin.models import User, Admin
from backend.admin.schemas import AdminSchema


admin_schema = AdminSchema()


class AdminRegistration(Resource):
    """Handle admin registration endpoints"""
    def post(self):
        json_data = request.get_json()
        if not json_data:
            abort(400, message="Empty request")

        data, errors = admin_schema.load(json_data)
        if errors:
            abort(422, message=errors)

        try:
            new_admin_user = User(
                full_name=data['full_name'],
                email=data['email'])
            db.session.add(new_admin_user)
            db.session.commit()

            hash_password = generate_password_hash(data['password'])
            new_admin_details = Admin(
                user_id=new_admin_user.id,
                password=hash_password)
            db.session.add(new_admin_details)
            db.session.commit()

            return {
                'message': "{} created successfully".format(data['full_name'])
            }, 201
        except Exception:
            abort(
                500, message="Admin not created due to internal server error")
