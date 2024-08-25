# src/repositories/user_repository.py

from sqlalchemy import or_
from sqlalchemy.orm import joinedload

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
        return User.query.filter_by(id=user_id).first()

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

    def get_user_with_grocery(self, user_id, load_groceries=False):
        """
        Get a user by their unique ID. Optionally, it can load groceries eagerly.
        :param user_id: The ID of the user.
        :param load_groceries: Boolean indicating whether to load groceries eagerly.
        return: The user object or None if not found.
        """
        user = self.db.session.query(User)
        if load_groceries:
            user = user.options(joinedload(User.user_groceries))

        return user.filter_by(id=user_id).first()

    def update_user(self, user):
        self.db.session.add(user)
        self.db.session.commit()
        return user

    def set_new_password(self, user, password):
        user.set_password(password)
        return self.update_user(user)

