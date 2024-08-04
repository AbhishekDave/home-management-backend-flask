# src/models/grocery_models/grocery_type_model.py

from src.configs.development_config import db


class GroceryType(db.Model):
    __tablename__ = 'grocery_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)


