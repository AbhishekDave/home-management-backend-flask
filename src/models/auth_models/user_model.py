# /src/models/auth_models/user_model.py

from datetime import datetime
from zoneinfo import ZoneInfo
from werkzeug.security import generate_password_hash, check_password_hash
from src.configs.development_config import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), unique=True, nullable=False, index=True)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    address = db.Column(db.String(255), nullable=True)
    phone = db.Column(db.String(255), unique=True, nullable=True)
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    last_login = db.Column(db.DateTime, default=datetime.now(ZoneInfo('UTC')))
    created_at = db.Column(db.DateTime, default=datetime.now(ZoneInfo('UTC')))
    modified_at = db.Column(db.DateTime, default=datetime.now(ZoneInfo('UTC')), onupdate=datetime.now(ZoneInfo('UTC')))

    user_groceries = db.relationship('GroceryName', backref=db.backref('user', lazy='joined'))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


"""
Use lazy='joined' when you expect a manageable number of related objects and want to optimize for the minimal number of queries.
Use lazy='subquery' when there are many related objects per parent, or when you want to avoid the overhead of a large JOIN result set.
"""
