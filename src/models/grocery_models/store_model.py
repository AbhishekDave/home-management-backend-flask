# src/models/grocery_models/store_model.py

from datetime import datetime
from zoneinfo import ZoneInfo
from src.configs.development_config import db


class Store(db.Model):
    __tablename__ = 'store'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    location = db.Column(db.String(80), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now(ZoneInfo('UTC')))
    modified_at = db.Column(db.DateTime, default=datetime.now(ZoneInfo('UTC')))

    products = db.relationship('Product', secondary='store_product_mapping', backref=db.backref('store', lazy='dynamic'))
