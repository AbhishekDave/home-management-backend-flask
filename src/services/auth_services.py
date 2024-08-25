# src/services/auth_services.py

from flask import current_app
import jwt
from src.configs.development_config import CURRENT_TIME_AT_TIMEZONE, ACCESS_EXPIRES_IN_5_MIN, REDIS_CLIENT
from src.services.user_services import UserService
from src.utils import NotFoundException, TokenUnauthorizedException


class AuthServices:
    def __init__(self, db):
        self.user_service = UserService(db)

    def create_forgot_password_token(self, username_or_email):
        user = self.user_service.find_user_by_username_or_email(username_or_email)
        if not user:
            raise NotFoundException('User not found')

        # Use the JWT secret key from the app config
        jwt_secret_key = current_app.config['JWT_SECRET_KEY']

        expiration_time = CURRENT_TIME_AT_TIMEZONE + ACCESS_EXPIRES_IN_5_MIN

        token = jwt.encode({
            'sub': user.id,
            'id': user.id,
            'exp': expiration_time,
        }, jwt_secret_key, algorithm='HS256')

        # Store token in Redis, associated with the user's ID
        REDIS_CLIENT.setex(f"forgot_password_token_for:{user.id}", ACCESS_EXPIRES_IN_5_MIN, token)

        return token

    @staticmethod
    def validate_forgot_password_token(token):
        try:
            # Use the JWT secret key from the app config
            jwt_secret_key = current_app.config['JWT_SECRET_KEY']

            decoded_token = jwt.decode(token, jwt_secret_key, algorithms=['HS256'])
            return decoded_token  # Contains user id or other info
        except jwt.ExpiredSignatureError:
            raise TokenUnauthorizedException('Token has expired')
        except jwt.InvalidTokenError:
            raise TokenUnauthorizedException('Invalid token')
