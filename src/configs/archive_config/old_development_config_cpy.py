# /src/configs/development_config.py

from datetime import timedelta
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": ["http://localhost:5173", "http://localhost:4173"]}})

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://tempuser:temppassword@localhost:3310/tempdatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = ''   # node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"

app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

ACCESS_EXPIRES_MINUTES = timedelta(minutes=1)
ACCESS_EXPIRES_HOURS = timedelta(hours=1)

db = SQLAlchemy(app)

jwt = JWTManager(app)

migrate = Migrate(app, db)

