from werkzeug.security import check_password_hash

from backend.admin.models import User, Admin


def authenticate(username, password):
    user = User.query.filter_by(email=username).first()
    admin_password = Admin.query.filter_by(user_id=user.id).first().password
    if user and check_password_hash(admin_password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return User.query.filter_by(id=user_id).first()
