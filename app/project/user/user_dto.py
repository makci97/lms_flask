from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'public_id': fields.String(description='user Identifier'),
        'username': fields.String(description='user username'),
        'password': fields.String(description='user password'),
        # 'verification_code': fields.String(description='user verification code'),

        'name': fields.String(required=True, description='user name'),
        'surname': fields.String(required=True, description='user surname'),
        'middle_name': fields.String(description='user middle name'),

        'email': fields.String(description='user email address'),
        'registered_on': fields.DateTime(description='user time registered on'),
        'admin': fields.Boolean(description='user has admin permissions', default=False),
    })
