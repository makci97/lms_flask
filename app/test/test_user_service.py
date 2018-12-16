import unittest

from app.project.user.user_service import UserService
from app.test.base import BaseTestCase


class TestUserService(BaseTestCase):
    def test_create_user_success(self):
        user_service = UserService()
        data = {
            'name': 'Ivan',
            'surname': 'Ivanov',
        }
        response, code = user_service.create_user(data)
        self.assertTrue(code == 201)

    def test_create_user_need_more_info(self):
        user_service = UserService()
        data = {
            'name': 'Ivan',
        }
        response, code = user_service.create_user(data)
        self.assertTrue(code == 400)

    def test_create_user_correct_responce(self):
        user_service = UserService()
        data = {
            'name': 'Ivan',
            'surname': 'Ivanov',
        }
        response, code = user_service.create_user(data)
        self.assertIsNotNone(response.get('public_id'))
        self.assertIsNotNone(response.get('verification_code'))

    def test_is_nan_user(self):
        user_service = UserService()
        self.assertTrue(user_service.is_nan_user())

        user_service = UserService()
        data = {
            'name': 'Ivan',
            'surname': 'Ivanov',
        }
        user_service.create_user(data)
        self.assertFalse(user_service.is_nan_user())

    def test_load_user(self):
        user_service = UserService()
        data = {
            'name': 'Ivan',
            'surname': 'Ivanov',
        }
        response, code = user_service.create_user(data)
        public_id = response.get('public_id')

        user_service = UserService()
        user_service.load_user(public_id)
        self.assertFalse(user_service.is_nan_user())


if __name__ == '__main__':
    unittest.main()
