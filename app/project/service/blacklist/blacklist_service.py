import datetime

import jwt

from app.project import db
from app.project.config import key
from app.project.model.blacklist.blacklist import BlacklistToken


class BlacklistService:
    @staticmethod
    def create_model_object(request):
        new_token = BlacklistToken(token=request['token'])
        return new_token

    @staticmethod
    def is_new(request):
        token = BlacklistToken.query.filter_by(token=request['token']).first()
        return token is None

    @staticmethod
    def apply_changes(model_object):
        db.session.add(model_object)
        db.session.commit()

    @staticmethod
    def save_token(request):
        if BlacklistService.is_new(request):
            new_token = BlacklistService.create_model_object(request)
            BlacklistService.apply_changes(new_token)

            response_object = {
                'status': 'success',
                'message': 'Successfully added to blacklist.'
            }
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'Token already exists.',
            }
            return response_object, 409

    @staticmethod
    def get_all_tokens():
        return BlacklistToken.query.all()

    @staticmethod
    def encode_auth_token(user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                key,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, key)
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token blacklisted. Please log in again.'
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
