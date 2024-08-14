from src.repositories.user_repository import UserRepository


class UserRetrievalService:
    def __init__(self, db):
        self.user_repository = UserRepository(db)

    def find_user_by_id(self, user_id):
        """
        Finds a user by their unique ID.

        :param user_id: The ID of the user.
        :return: The user object or None if not found.
        """
        return self.user_repository.get_user_by_id(user_id)

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
