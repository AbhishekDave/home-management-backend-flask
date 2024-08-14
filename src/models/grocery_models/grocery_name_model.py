# src/models/grocery_models/grocery_name_model.py

from datetime import datetime
from zoneinfo import ZoneInfo
from src.configs.development_config import db


class GroceryName(db.Model):
    __tablename__ = 'grocery_name'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)    # ABC List, GYM List, etc
    type = db.Column(db.String(80), unique=True, nullable=False)    # Weekly, Monthly, Daily, etc
    created_at = db.Column(db.DateTime, default=datetime.now(ZoneInfo('UTC')))
    modified_at = db.Column(db.DateTime, default=datetime.now(ZoneInfo('UTC')))
    is_active = db.Column(db.Boolean, default=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
