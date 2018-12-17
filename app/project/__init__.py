from flask import Flask
from flask_bcrypt import Bcrypt
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy

from .config import config_by_name
from .user.user_service import UserService

db = SQLAlchemy()
flask_bcrypt = Bcrypt()
auth = HTTPBasicAuth()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)

    return app


@auth.verify_password
def verify_pw(email, password):
    return UserService.check_email_password_pair(email, password)
