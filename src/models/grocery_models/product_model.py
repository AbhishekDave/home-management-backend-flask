# src/models/grocery_models/product_model.py

from src.configs.development_config import db


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    product_type = db.Column(db.String(80), nullable=False)
    expiry_date = db.Column(db.Date, nullable=False)
    grocery_type_id = db.Column(db.Integer, db.ForeignKey('grocery_type.id'), nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'), nullable=False)

    stores = db.relationship('Store', backref=db.backref('products', lazy='dynamic'))
    grocery_types = db.relationship('GroceryType', backref=db.backref('products', lazy='dynamic'))
