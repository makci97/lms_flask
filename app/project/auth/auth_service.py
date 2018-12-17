from functools import wraps

from app.project.user.user_service import UserService
from . import auth


class AuthService:
    @staticmethod
    def check_email_password_pair(email, password):
        user = UserService.get_user_by_email(email)
        return (user is not None) and user.check_password(password)

    @staticmethod
    def is_admin(email):
        user = UserService.get_user_by_email(email)
        return (user is not None) and user.admin

    @staticmethod
    def admin_permission_required(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            email = auth.email()
            if not AuthService.is_admin(email):
                response_object = {
                    'status': 'fail',
                    'message': 'permission denied'
                }
                return response_object, 403

            return f(*args, **kwargs)

        return decorated

    @staticmethod
    def sign_up_user(data):
        user_service = UserService()
        return user_service.sign_up(data)
