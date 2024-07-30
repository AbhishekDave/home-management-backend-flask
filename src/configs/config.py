# src/configs/config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    class MySQLConfig:
        MYSQL_ROOT_PASSWORD = os.getenv('MYSQL_ROOT_PASSWORD')
        MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')
        MYSQL_USER = os.getenv('MYSQL_USER')
        MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')

    class JWTConfig:
        JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
        JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES', 1))  # in minutes
        JWT_REFRESH_TOKEN_EXPIRES = int(os.getenv('JWT_REFRESH_TOKEN_EXPIRES', 30))  # in days

    class REDISConfig:
        REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')  # Default to 'localhost' if not set
        REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))  # Default to 6379 if not set
        REDIS_DB = int(os.getenv('REDIS_DB', 0))  # Default to 0 if not set
        REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', None)  # Default to None if not set
