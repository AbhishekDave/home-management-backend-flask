# src/models/grocery_models/store_model.py

from src.configs.development_config import db


class Store(db.Model):
    __tablename__ = 'store'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    location = db.Column(db.String(80), nullable=True)



