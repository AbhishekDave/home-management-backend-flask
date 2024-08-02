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
from src.utils import common_error_handlers     # , jwt_error_handlers  # Import Error handler class

# Just Import models to attach with flask migrate
import src.models

app = Flask(__name__)

# CORS configuration
CORS(app, resources={r"/*": {"origins": [f"{cors_config.CORSConfig.CORS_FRONTEND_URL_DEV_ENV}"]}})

# Database URI
app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{database_config.MySQLConfig.MYSQL_USER}:{database_config.MySQLConfig.MYSQL_PASSWORD}@localhost:3310/{database_config.MySQLConfig.MYSQL_DATABASE}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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

# JWT configuration
# node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"
app.config['JWT_SECRET_KEY'] = jwt_config.JWTConfig.JWT_SECRET_KEY
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(seconds=jwt_config.JWTConfig.ACCESS_TOKEN_EXPIRES_IN_1_DAY)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=jwt_config.JWTConfig.REFRESH_TOKEN_EXPIRES_IN_30_DAY)

print(f"\nJWT Expire in {app.config["JWT_ACCESS_TOKEN_EXPIRES"]}")

# Access token expiration settings
CURRENT_TIME_AT_TIMEZONE = datetime.now(ZoneInfo('UTC'))
ACCESS_EXPIRES_MINUTES = timedelta(minutes=jwt_config.JWTConfig.ACCESS_TOKEN_EXPIRES_IN_1_DAY)
REFRESH_EXPIRES_DAYS = timedelta(days=jwt_config.JWTConfig.REFRESH_TOKEN_EXPIRES_IN_30_DAY)

# Initialize Redis
redis_client = redis_config.REDISConfig.redis_client  # Access the redis_client from REDISConfig

# Set up SQLAlchemy
db = SQLAlchemy(app)

# Set up JWT
jwt = JWTManager(app)

# Set up Flask-Migrate
migrate = Migrate(app, db)

# Centralizing Error handlers for my app
common_error_handlers.ErrorHandlers.register_error_handlers(app)
# JWTErrorHandlers.register_error_handlers(app)
