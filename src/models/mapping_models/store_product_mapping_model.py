# src/models/mapping_models/store_product_mapping_model.py

from datetime import datetime
from zoneinfo import ZoneInfo

from sqlalchemy import Index

from src.configs.development_config import db


class StoreProductMapping(db.Model):
    __tablename__ = 'store_product_mapping'
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'), nullable=False, index=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False, index=True)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    expiry_date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(ZoneInfo('UTC')))
    modified_at = db.Column(db.DateTime, default=datetime.now(ZoneInfo('UTC')), onupdate=datetime.now(ZoneInfo('UTC')))

    __table_args__ = (
        Index('ix_store_product', 'store_id', 'product_id'),  # Composite index
    )
