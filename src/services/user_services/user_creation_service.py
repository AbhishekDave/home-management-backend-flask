from src.repositories.user_repository import UserRepository
from src.models.auth_models.user_model import User


class UserCreationService:
    def __init__(self, db):
        self.user_repository = UserRepository(db)

    def create_user(self, user_data):
        """
        Creates a new user and saves it to the database.

        :param user_data: Dictionary containing user information.
        :return: The created user object.
        """
        user = User(**user_data)
        user.set_password(user_data['password'])
        self.user_repository.add_user(user)
        return user
