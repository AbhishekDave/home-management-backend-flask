# src/decorators/auth_decorators/auth_requires_at_forgot_password.py

from functools import wraps
from flask import request, g

from src.configs.development_config import db
from src.services.user_services import UserService
from src.utils import TokenUnauthorizedException, MethodNotAllowedException, MissingDataException, NotFoundException


def auth_requires_at_forgot_password(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if request.method != 'POST':
            raise MethodNotAllowedException('Method Not Allowed')

        user_service = UserService(db)
        user_data = request.get_json()

        if not user_data:
            raise MissingDataException('No input data provided.')

        username_or_email = user_data.get('username')

        user = user_service.find_user_by_username_or_email(username_or_email)
        if not user:
            raise NotFoundException('User not found.')

        g.user_data = user.email

        return f(*args, **kwargs)
    return decorated


