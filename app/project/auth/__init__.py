from flask import request
from flask_httpauth import HTTPBasicAuth

from .auth_service import AuthService


class HTTPEmailPassAuth(HTTPBasicAuth):
    def email(self):
        if not request.authorization:
            return ""
        return request.authorization.email


auth = HTTPEmailPassAuth()


@auth.verify_password
def verify_pw(email, password):
    return AuthService.check_email_password_pair(email, password)
