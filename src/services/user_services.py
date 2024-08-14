from marshmallow import ValidationError
from src.repositories.user_repository import UserRepository, User
from src.schemas.auth_schemas.complete_user_schema import CompleteUserSchema
from src.schemas.auth_schemas.user_login_schema import UserLoginSchema
from src.schemas.auth_schemas.user_registration_schema import UserRegistrationSchema


class UserService:
    def __init__(self, db):
        self.user_repository = UserRepository(db)
        self.complete_user_schema = CompleteUserSchema()
        self.user_login_schema = UserLoginSchema()
        self.user_registration_schema = UserRegistrationSchema()

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

    # UPDATE Operations
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

    # DELETE Operations
    # Implement delete operations if needed, e.g., def delete_user(self, user_id): ...

    # Serialization Operations
    def dump_complete_user_schema(self, user):
        """
        Serializes a user object using the CompleteUserSchema.

        :param user: The user object to serialize.
        :return: Serialized user data.
        """
        return self.complete_user_schema.dump(user)

    def dump_user_registration_schema(self, user):
        """
        Serializes a user object using the UserRegistrationSchema.

        :param user: The user object to serialize.
        :return: Serialized user data.
        """
        return self.user_registration_schema.dump(user)

    def dump_user_login_schema(self, user):
        """
        Serializes a user object using the UserLoginSchema.

        :param user: The user object to serialize.
        :return: Serialized user data.
        """
        return self.user_login_schema.dump(user)

    @staticmethod
    def dump_all_users(user, fields=None):
        """
        Serializes the user object using the CompleteUserSchema.

        :param user: The user object to serialize.
        :param fields: Optional list of fields to include in the output.
        :return: Serialized user data.
        """
        if not fields:
            schema = CompleteUserSchema()
        else:
            schema = CompleteUserSchema(only=fields)

        return schema.dump(user)
