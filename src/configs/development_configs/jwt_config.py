# src/configs/development_configs/jwt_config.py

import os
from dotenv import load_dotenv

load_dotenv()


class JWTConfig:
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    ACCESS_TOKEN_EXPIRES_IN_1_MIN = int(os.environ.get('JWT_ACCESS_TOKEN_EXPIRES', 60))  # Default to 1 Min
    ACCESS_TOKEN_EXPIRES_IN_1_HOUR = int(os.environ.get('JWT_ACCESS_TOKEN_EXPIRES', 3600))  # Default to 1 hour
    ACCESS_TOKEN_EXPIRES_IN_1_DAY = int(os.environ.get('JWT_ACCESS_TOKEN_EXPIRES', 86400))  # Default to 1 hour
    REFRESH_TOKEN_EXPIRES_IN_1_HOUR = int(os.environ.get('JWT_ACCESS_TOKEN_EXPIRES', 3600))  # Default to 1 hour
    REFRESH_TOKEN_EXPIRES_IN_1_DAY = int(os.environ.get('JWT_REFRESH_TOKEN_EXPIRES', 86400))  # Default to 1 day
    REFRESH_TOKEN_EXPIRES_IN_30_DAY = int(os.environ.get('JWT_REFRESH_TOKEN_EXPIRES', 2592000))  # Default to 30 day

