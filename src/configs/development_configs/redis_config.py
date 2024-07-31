import os


class REDISConfig:
    REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')  # Default to 'localhost' if not set
    REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))  # Default to 6379 if not set
    REDIS_DB = int(os.getenv('REDIS_DB', 0))  # Default to 0 if not set
    REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', None)  # Default to None if not set
