from src.repositories.user_repository import UserRepository


class UserAuthenticationService:
    def __init__(self, db):
        self.user_repository = UserRepository(db)

    def authenticate_user(self, username_or_email, password):
        """
        Authenticates a user by checking their username/email and password.

        :param username_or_email: The username or email of the user.
        :param password: The password of the user.
        :return: The authenticated user object or None if authentication fails.
        """
        user = (self.user_repository.get_user_by_username(username_or_email) or
                self.user_repository.get_user_by_email(username_or_email))
        if user and user.check_password(password):
            return user
        return None
