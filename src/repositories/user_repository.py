# src/repositories/user_repository.py

from sqlalchemy import or_
from src.models.auth_models.user_model import User


class UserRepository:
    def __init__(self, db):
        self.db = db

    def add_user(self, user):
        self.db.session.add(user)
        self.db.session.commit()

    def get_all_users(self):
        return self.db.session.query(User).all()

    @staticmethod
    def get_user_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_user_by_username_or_email(username_or_email: str) -> User:
        # Query the User model to find a user by username or email
        user = User.query.filter(
            or_(
                User.username == username_or_email,
                User.email == username_or_email
            )
        ).first()

        print(user)

        return User.query.filter(
            or_(
                User.username == username_or_email,
                User.email == username_or_email
            )
        ).first()

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    def delete_user(self, user_id):
        user = self.get_user_by_id(user_id)
        if user:
            self.db.session.delete(user)
            self.db.session.commit()

    @staticmethod
    def calculate_user_age(birthdate):
        # Perform some static calculation or utility function
        from datetime import datetime
        today = datetime.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age
