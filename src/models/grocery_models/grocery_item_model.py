# src/models/grocery_models/grocery_item_model.py

from datetime import datetime
from zoneinfo import ZoneInfo
from src.configs.development_config import db


class GroceryItem(db.Model):
    __tablename__ = 'grocery_item'

    id = db.Column(db.Integer, primary_key=True)
    grocery_name_id = db.Column(db.Integer, db.ForeignKey('grocery_name.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    created_at = db.Column(db.DateTime, default=datetime.now(ZoneInfo('UTC')))
    modified_at = db.Column(db.DateTime, default=datetime.now(ZoneInfo('UTC')))
