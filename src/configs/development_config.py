# /src/configs/development_config.py

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://tempuser:temppassword@localhost:3310/tempdatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = '6e982988192d4729f69ba54dfd292757ff0b3a8f68ce9272f0e752cd49bb27eb'   # node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"

db = SQLAlchemy(app)

jwt = JWTManager(app)

migrate = Migrate(app, db)

