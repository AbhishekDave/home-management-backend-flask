# src/configs/development_configs/cors_config.py

import os
from dotenv import load_dotenv

load_dotenv()


class CORSConfig:
    CORS_FRONTEND_URL_DEV_ENV = os.environ.get('CORS_FRONTEND_URL_DEV_ENV')
