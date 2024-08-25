# src/services/serialization_services/user_serialization.py

from src.schemas.auth_schemas.user_schema import UserSchema
from src.schemas.auth_schemas.user_registration_schema import UserRegistrationSchema
from src.schemas.auth_schemas.user_login_schema import UserLoginSchema


class UserSerializationService:
    def __init__(self):
        self.complete_user_schema = self._get_user_schema()
        self.user_login_schema = self._get_user_login_schema()
        self.user_registration_schema = self._get_user_registration_schema()

    @staticmethod
    def _get_user_schema():
        from src.schemas.auth_schemas.user_schema import UserSchema
        return UserSchema()

    @staticmethod
    def _get_user_login_schema():
        from src.schemas.auth_schemas.user_login_schema import UserLoginSchema
        return UserLoginSchema()

    @staticmethod
    def _get_user_registration_schema():
        from src.schemas.auth_schemas.user_registration_schema import UserRegistrationSchema
        return UserRegistrationSchema()

    def dump_user_registration_schema(self, user):
        return self.user_registration_schema.dump(user)

    def serialize_user_data(self, user, fields=None):
        schema = self._get_user_schema()
        if fields:
            schema = UserSchema(many=True, exclude=fields)
        return schema.dump(user)

    def serialize_user_registration_data(self, user, fields=None):
        schema = self._get_user_registration_schema()
        if fields:
            schema = UserRegistrationSchema(many=False, exclude=fields)
        return schema.dump(user)
