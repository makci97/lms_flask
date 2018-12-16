import datetime
import unittest

from app.project import db
from app.project.service.blacklist.blacklist_service import BlacklistService
from app.project.user.user_model import User
from app.project.user.user_service import UserService
from app.test.base import BaseTestCase


class TestBlacklistService(BaseTestCase):

    def test_encode_auth_token(self):
        request = dict(
            email='test@test.com',
            password='test',
            registered_on=datetime.datetime.utcnow()
        )
        UserService.save_user(request)
        db.session.add(user)
        db.session.commit()
        auth_token = BlacklistService.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))

    def test_decode_auth_token(self):
        user = User(
            email='test@test.com',
            password='test',
            registered_on=datetime.datetime.utcnow()
        )
        db.session.add(user)
        db.session.commit()
        auth_token = BlacklistService.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertTrue(BlacklistService.decode_auth_token(auth_token.decode("utf-8") ) == 1)


if __name__ == '__main__':
    unittest.main()
