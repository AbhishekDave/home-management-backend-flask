# src/models/grocery_models/grocery_item_model.py

from datetime import datetime
from zoneinfo import ZoneInfo

from sqlalchemy import Index

from src.configs.development_config import db


class GroceryItem(db.Model):
    __tablename__ = 'grocery_item'

    id = db.Column(db.Integer, primary_key=True)
    grocery_name_id = db.Column(db.Integer, db.ForeignKey('grocery_name.id'), index=True)
    item_id = db.Column(db.Integer, db.ForeignKey('product.id'), index=True)
    created_at = db.Column(db.DateTime, default=datetime.now(ZoneInfo('UTC')))
    modified_at = db.Column(db.DateTime, default=datetime.now(ZoneInfo('UTC')), onupdate=datetime.now(ZoneInfo('UTC')))

    __table_args__ = (
        # Composite index might be useful if you often query by both grocery_name_id and item_id together
        Index('ix_grocery_item', 'grocery_name_id', 'item_id'),
    )
