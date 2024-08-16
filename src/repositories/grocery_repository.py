# src/repositories/grocery_repository.py

# from sqlalchemy import or_
from src.models.grocery_models.grocery_name_model import GroceryName


class GroceryRepository:
    def __init__(self, db):
        self.db = db

    def add_grocery_name(self, grocery_name_data):
        self.db.session.add(grocery_name_data)
        self.db.session.commit()

    def get_all_grocery_names(self):
        return self.db.session.query(GroceryName).all()

    def get_all_grocery_names_by_user(self, user_id):
        return self.db.session.query(GroceryName).filter_by(user_id=user_id).all()

    def get_grocery_name_by_user_and_name(self, user_id, name):
        """
        Checks if a grocery name with the given name and type exists for the current user.
        """
        return self.db.session.query(GroceryName).filter_by(user_id=user_id, name=name).first()
