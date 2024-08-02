# src/models/mapping_models/user_grocery_type_model.py

from src.configs.development_config import db


class UserGroceryType(db.Model):
    __tablename__ = 'user_grocery_type'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    grocery_type_id = db.Column(db.Integer, db.ForeignKey('grocery_type.id'), nullable=False)


