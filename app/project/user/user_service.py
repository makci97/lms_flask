import datetime
import uuid

from app.project import db
from app.project.user.user_model import User


# admin = db.Column(db.Boolean, nullable=False, default=False)

class UserService:
    def __init__(self):
        self.user = None

    def create_user(self, data):
        if self._data_verification(data):
            self._create_model_object(data)
        else:
            response_object = {
                'status': 'fail',
                'message': 'Please give all needed info.'
            }
            return response_object, 400

        self._save_changes()

        response_object = {
            'status': 'success',
            'public_id': self.user.public_id,
            'verification_code': self.user.verification_code,
            'message': 'Successfully created.'
        }
        return response_object, 201

    def load_user(self, public_id):
        self.user = User.query.filter_by(public_id=public_id).first()

    def is_nan_user(self):
        return self.user is None

    def get_user(self):
        return self.user

    def _data_verification(self, data):
        if 'name' not in data or 'surname' not in data:
            return False
        return True

    def _create_model_object(self, data):
        user_data = dict(
            public_id=str(uuid.uuid4()),
            verification_code=str(uuid.uuid4()),
            registered_on=datetime.datetime.utcnow()
        )
        user_data.update(data)
        self.user = User(**user_data)

    def _save_changes(self):
        db.session.add(self.user)
        db.session.commit()

    @staticmethod
    def get_all_users():
        return User.query.all()
