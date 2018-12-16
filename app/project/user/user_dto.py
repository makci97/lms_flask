from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'public_id': fields.String(required=True, description='user Identifier'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'verification_code': fields.String(description='user verification code'),

        'name': fields.String(required=True, description='user name'),
        'surname': fields.String(required=True, description='user surname'),
        'middle_name': fields.String(description='user middle name'),

        'email': fields.String(required=True, description='user email address'),
        'registered_on': fields.DateTime(required=True, description='user time registered on'),
        'admin': fields.String(required=True, description='user has admin permissions'),
    })
