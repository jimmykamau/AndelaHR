import os

from flask import Flask
from flask_jwt import JWT
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
db = SQLAlchemy(app)


from backend.admin.endpoints import AdminRegistration
from backend.user.endpoints import UserCreation
from backend.utils import authenticate, identity


jwt = JWT(app, authenticate, identity)

api.add_resource(UserCreation, '/user/')
api.add_resource(AdminRegistration, '/auth/register/')


if __name__ == '__main__':
    app.run()
