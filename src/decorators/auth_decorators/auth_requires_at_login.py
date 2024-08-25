# src/decorators/auth_decorators/auth_requires_at_login.py

from functools import wraps
from flask import request, g

from src.configs.development_config import db
from src.services.user_services import UserService
from src.utils.error_handling_utility.exceptions import (MethodNotAllowedException, CredentialsUnauthorizedException, MissingDataException)


def auth_requires_at_login(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if request.method != 'POST':
            raise MethodNotAllowedException('Method not allowed.')

        user_service = UserService(db)
        user_data = request.get_json()
        if not user_data:
            raise MissingDataException('No input data provided.')

        username = user_data.get('username')
        password = user_data.get('password')

        # Check if the user logging with correct username or email
        user = user_service.authenticate_user(username, password)
        if user is None:
            raise CredentialsUnauthorizedException('Invalid credentials, please try again.')

        # Check if the user is active or not
        print(user.is_active)

        if not user.is_active:
            raise CredentialsUnauthorizedException('Oops, User\'\'s account is inactive, Please contact admin.')

        g.user = user  # Attach the user to the request for use in the view function

        return f(*args, **kwargs)

    return decorated
