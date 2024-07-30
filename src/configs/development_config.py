from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import redis
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from src.configs.config import Config  # Import the Config class

app = Flask(__name__)

# CORS configuration
CORS(app, resources={r"/*": {"origins": ["http://localhost:5173", "http://localhost:4173"]}})

# Database URI
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{Config.MySQLConfig.MYSQL_USER}:{Config.MySQLConfig.MYSQL_PASSWORD}@localhost:3310/{Config.MySQLConfig.MYSQL_DATABASE}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# JWT configuration
app.config['JWT_SECRET_KEY'] = Config.JWTConfig.JWT_SECRET_KEY   # node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=Config.JWTConfig.JWT_ACCESS_TOKEN_EXPIRES)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=Config.JWTConfig.JWT_REFRESH_TOKEN_EXPIRES)

# Access token expiration settings
CURRENT_TIME_AT_TIMEZONE = datetime.now(ZoneInfo('UTC'))
ACCESS_EXPIRES_MINUTES = timedelta(minutes=1)
ACCESS_EXPIRES_HOURS = timedelta(hours=1)

# Initialize Redis
redis_client = redis.StrictRedis(
    host=Config.REDISConfig.REDIS_HOST,
    port=Config.REDISConfig.REDIS_PORT,
    db=Config.REDISConfig.REDIS_DB,
    password=Config.REDISConfig.REDIS_PASSWORD,
    decode_responses=True
)


# Set up SQLAlchemy
db = SQLAlchemy(app)

# Set up JWT
jwt = JWTManager(app)

# Set up Flask-Migrate
migrate = Migrate(app, db)
