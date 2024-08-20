# src/configs/development_config.py

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from sqlalchemy import create_engine

from src.configs.development_configs import database_config, jwt_config, redis_config, cors_config
from src.configs.development_configs.cors_config import CORSConfig
from src.utils.error_handling_utility import common_error_handlers

from src.utils.logging_utility.configure_logging import configure_logging

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

# Global Configuration
API_VERSION_1 = CORSConfig.API_VERSION

# JWT configuration
# node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"
CURRENT_TIME_AT_TIMEZONE = datetime.now(ZoneInfo('UTC'))
ACCESS_EXPIRES_MINUTES = timedelta(days=jwt_config.JWTConfig.ACCESS_TOKEN_EXPIRES_IN_1_DAY)
REFRESH_EXPIRES_DAYS = timedelta(days=jwt_config.JWTConfig.REFRESH_TOKEN_EXPIRES_IN_30_DAY)

# Redis Client
REDIS_CLIENT = redis_config.REDISConfig.redis_client


def create_app():
    app = Flask(__name__)

    # Database URI configuration
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{database_config.MySQLConfig.MYSQL_USER}:{database_config.MySQLConfig.MYSQL_PASSWORD}@localhost:3310/{database_config.MySQLConfig.MYSQL_DATABASE}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # JWT configuration
    app.config['JWT_SECRET_KEY'] = jwt_config.JWTConfig.JWT_SECRET_KEY
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=jwt_config.JWTConfig.ACCESS_TOKEN_EXPIRES_IN_1_DAY)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=jwt_config.JWTConfig.REFRESH_TOKEN_EXPIRES_IN_30_DAY)

    # Initialize database, flask-migrate and JWT extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Configure Logging
    configure_logging(app)

    # CORS configuration
    CORS(app, resources={r"/*": {"origins": [f"{cors_config.CORSConfig.CORS_FRONTEND_URL_DEV_ENV}"]}})

    # Test database connection
    try:
        engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
        print('\n')
        print(engine)
        connection = engine.connect()
        print('\n')
        print(engine)
        print("\nConnection successful!")
        connection.close()
    except Exception as e:
        print(f"\nError: {e}")

    # Centralizing Error handlers for my app
    common_error_handlers.ErrorHandlers.register_error_handlers(app)
    # JWTErrorHandlers.register_error_handlers(app)

    # Import models here to avoid circular imports
    with app.app_context():
        pass

    return app
