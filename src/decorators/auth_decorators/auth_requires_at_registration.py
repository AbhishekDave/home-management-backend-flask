# # src/decorators/auth_decorators/auth_requires_at_registration.py

from functools import wraps
from flask import request

from src.configs.development_config import db
from src.utils.error_handling_utility.exceptions import MissingDataException, ConflictException
from src.services.user_services import UserService


def auth_requires_at_registration(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        user_service = UserService(db)
        user_data = request.get_json()
        if not user_data:
            raise MissingDataException('No input data provided.')

        user_by_username = user_service.find_user_by_username(user_data['username'])
        user_by_email = user_service.find_user_by_email(user_data['email'])

        if user_by_username or user_by_email:
            raise ConflictException('User already exists.')

        return f(*args, **kwargs)

    return decorated
