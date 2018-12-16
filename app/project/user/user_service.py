import datetime
import uuid

from app.project import db
from app.project.user.user_model import User


# admin = db.Column(db.Boolean, nullable=False, default=False)

class UserService:
    @staticmethod
    def create_model_object(request):
        new_user = User(
            public_id=str(uuid.uuid4()),
            username=request['username'],
            password=request['password'],
            verification_code=str(uuid.uuid4()),
            name=request['name'],
            surname=request['surname'],
            middle_name=request['middle_name'],
            email=request['email'],
            registered_on=datetime.datetime.utcnow()
        )
        return new_user

    @staticmethod
    def is_new(request):
        user = User.query.filter_by(username=request['username']).first()
        return user is None

    @staticmethod
    def apply_changes(model_object):
        db.session.add(model_object)
        db.session.commit()

    @staticmethod
    def save_user(request):
        if UserService.is_new(request):
            new_user = UserService.create_model_object(request)
            UserService.apply_changes(new_user)

            response_object = {
                'status': 'success',
                'message': 'Successfully registered.'
            }
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'User already exists. Please Log in.',
            }
            return response_object, 409

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def get_user(public_id):
        return User.query.filter_by(public_id=public_id).first()
