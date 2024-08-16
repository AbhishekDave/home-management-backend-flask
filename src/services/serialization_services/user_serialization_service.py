# src/services/serialization_services/user_serialization.py

from src.schemas.auth_schemas.complete_user_schema import CompleteUserSchema
from src.schemas.auth_schemas.user_login_schema import UserLoginSchema
from src.schemas.auth_schemas.user_registration_schema import UserRegistrationSchema


class UserSerializationService:
    def __init__(self):
        self.complete_user_schema = CompleteUserSchema()
        self.user_login_schema = UserLoginSchema()
        self.user_registration_schema = UserRegistrationSchema()

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
