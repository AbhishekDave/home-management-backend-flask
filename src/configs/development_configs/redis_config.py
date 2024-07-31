# src/configs/development_configs/redis_config.py

import os
import redis
from dotenv import load_dotenv

load_dotenv()


class REDISConfig:
    REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')  # Default to 'localhost' if not set
    REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))  # Default to 6379 if not set
    REDIS_DB = int(os.getenv('REDIS_DB', 0))  # Default to 0 if not set
    REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', None)  # Default to None if not set

    # Initialize Redis
    redis_client = redis.StrictRedis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        db=REDIS_DB,
        password=REDIS_PASSWORD,
        decode_responses=True
    )
