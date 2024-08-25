# src/services/user_services.py

from flask_jwt_extended import get_jwt_identity

from src.repositories.user_repository import UserRepository, User
from src.utils import NotFoundException


class UserService:
    def __init__(self, db):
        self.user_repository = UserRepository(db)

    # CREATE Operations
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

    # READ Operations
    def authenticate_user(self, username_or_email, password):
        """
        Authenticates a user by checking their username/email and password.

        :param username_or_email: The username or email of the user.
        :param password: The password of the user.
        :return: The authenticated user object or None if authentication fails.
        """
        user = self.find_user_by_username_or_email(username_or_email)
        if user and user.check_password(password):
            return user
        return None

    @staticmethod
    def find_current_user_id():
        current_user = get_jwt_identity()
        return current_user

    def find_user_by_id(self, user_id):
        """
        Finds a user by their unique ID.

        :param user_id: The ID of the user.
        :return: The user object or None if not found.
        """
        user = self.user_repository.get_user_by_id(user_id)
        if not user:
            raise NotFoundException('User not found.')
        return user

    def find_user_by_username(self, username):
        """
        Finds a user by their username.

        :param username: The username of the user.
        :return: The user object or None if not found.
        """
        return self.user_repository.get_user_by_username(username)

    def find_user_by_email(self, email):
        """
        Finds a user by their email.

        :param email: The email of the user.
        :return: The user object or None if not found.
        """
        return self.user_repository.get_user_by_email(email)

    def find_user_by_username_or_email(self, username_or_email):
        """
        Finds a user by either their username or email.

        :param username_or_email: The username or email of the user.
        :return: The user object or None if not found.
        """
        return (self.user_repository.get_user_by_username(username_or_email) or
                self.user_repository.get_user_by_email(username_or_email))

    def find_all_users(self):
        """
        Retrieves all users from the database.

        :return: A list of all user objects.
        """
        return self.user_repository.get_all_users()

    def find_user_with_groceries(self, user_id):
        """
        Searches for a user by their grocery.
        :param user_id: The ID of the user.
        :return: The user object with groceries as a List or None if not found.
        """
        user = self.user_repository.get_user_with_grocery(user_id, load_groceries=True)
        if not user:
            raise NotFoundException(f'User_ID {user_id} not found.')
        return user

# UPDATE Operations
    def update_new_password(self, username_or_email, new_password):
        """
        Updates a user's password.
        :param username_or_email: The user's username or email.
        :param new_password: The new password.
        :return: The updated user object.
        """
        user = self.find_user_by_username_or_email(username_or_email)
        if not user:
            raise NotFoundException(f'User_ID {username_or_email} not found.')
        self.user_repository.set_new_password(user, new_password)
        return user


# DELETE Operations
# Implement delete operations if needed, e.g., def delete_user(self, user_id): ...

"""    def find_user_with_groceries(self, user_id):

        Searches for a user by their groceries.
        :param user_id: The ID of the user.
        :return: The user object with groceries as a List or None if not found.

        from src.services.grocery_services import GroceryService
        grocery_service = GroceryService(db)
        user = self.find_user_by_id(user_id)
        if not user:
            raise NotFoundException(f'User_ID {user_id} not found.')

        grocery_lists = grocery_service.find_all_grocery_names_by_user_id(user_id)
        user.user_groceries = grocery_lists
        return user
    """
