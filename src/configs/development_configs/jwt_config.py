# src/configs/development_configs/jwt_config.py

import os
from dotenv import load_dotenv

load_dotenv()


class JWTConfig:
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    ACCESS_TOKEN_EXPIRES_IN_1_MIN = int(os.environ.get('JWT_ACCESS_TOKEN_EXPIRES', 1))  # Default to 1 Min
    ACCESS_TOKEN_EXPIRES_IN_5_MIN = int(os.environ.get('JWT_ACCESS_TOKEN_EXPIRES', 5))  # Default to 5 Min
    ACCESS_TOKEN_EXPIRES_IN_1_HOUR = int(os.environ.get('JWT_ACCESS_TOKEN_EXPIRES', 1))  # Default to 1 hour
    ACCESS_TOKEN_EXPIRES_IN_1_DAY = int(os.environ.get('JWT_ACCESS_TOKEN_EXPIRES', 1))  # Default to 1 Day
    REFRESH_TOKEN_EXPIRES_IN_1_HOUR = int(os.environ.get('JWT_ACCESS_TOKEN_EXPIRES', 1))  # Default to 1 hour
    REFRESH_TOKEN_EXPIRES_IN_1_DAY = int(os.environ.get('JWT_REFRESH_TOKEN_EXPIRES', 1))  # Default to 1 day
    REFRESH_TOKEN_EXPIRES_IN_30_DAY = int(os.environ.get('JWT_REFRESH_TOKEN_EXPIRES', 30))  # Default to 30 day

