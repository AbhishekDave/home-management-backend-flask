# src/models/grocery_models/product_model.py

from datetime import datetime
from zoneinfo import ZoneInfo
from src.configs.development_config import db


class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False, index=True)
    product_type = db.Column(db.String(80), nullable=False, index=True)
    created_at = db.Column(db.DateTime, default=datetime.now(ZoneInfo('UTC')))
    modified_at = db.Column(db.DateTime, default=datetime.now(ZoneInfo('UTC')), onupdate=datetime.now(ZoneInfo('UTC')))

    grocery_items_as_product = db.relationship('GroceryItem', backref=db.backref('product', lazy='joined'))
