# src/services/user_service.py

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

    def authenticate_user(self, username_or_email, password):
        # Fetch the user by username or email
        user = (self.user_repository.get_user_by_username(username_or_email) or
                self.user_repository.get_user_by_email(username_or_email))

        # Check if user is None
        if user is None:
            return None  # User not found, handle this case in your controller

        # Check the password
        if user.check_password(password):
            return user

        return None  # Invalid password

    def create_user(self, user_data):
        user = User(**user_data)
        user.set_password(user_data['password'])
        self.user_repository.add_user(user)
        return user

    def dump_complete_user_schema(self, user):
        return self.complete_user_schema.dump(user)

    def dump_user_registration_schema(self, user):
        return self.user_registration_schema.dump(user)

    def dump_user_login_schema(self, user):
        return self.user_login_schema.dump(user)

    def dump_all_users(self, users):
        return self.complete_user_schema.dump(users)

    def find_user_by_username(self, user):
        return self.user_repository.get_user_by_username(user)

    def find_user_by_email(self, email):
        return self.user_repository.get_user_by_email(email)

    def find_user_by_username_or_email(self, username_or_email):
        user = self.user_repository.get_user_by_username_or_email(username_or_email)
        print(user)
        return self.user_repository.get_user_by_username_or_email(username_or_email)

    def find_user_by_id(self, user_id):
        return self.user_repository.get_user_by_id(user_id)

    def find_all_users(self):
        return self.user_repository.get_all_users()
