# config/jwt_config.py
import os


class JWTConfig:
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    ACCESS_TOKEN_EXPIRES = int(os.environ.get('JWT_ACCESS_TOKEN_EXPIRES', 3600))  # Default to 1 hour
    REFRESH_TOKEN_EXPIRES = int(os.environ.get('JWT_REFRESH_TOKEN_EXPIRES', 86400))  # Default to 1 day
