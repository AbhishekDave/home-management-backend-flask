# src/services/serialization_services/user_serialization.py

from src.schemas.auth_schemas.user_schema import UserSchema


class UserSerializationService:
    def __init__(self):
        self.complete_user_schema = self._get_user_schema()
        self.user_login_schema = self._get_user_login_schema()
        self.user_registration_schema = self._get_user_registration_schema()

    def _get_user_schema(self):
        from src.schemas.auth_schemas.user_schema import UserSchema
        return UserSchema()

    def _get_user_login_schema(self):
        from src.schemas.auth_schemas.user_login_schema import UserLoginSchema
        return UserLoginSchema()

    def _get_user_registration_schema(self):
        from src.schemas.auth_schemas.user_registration_schema import UserRegistrationSchema
        return UserRegistrationSchema()

    def dump_user_registration_schema(self, user):
        return self.user_registration_schema.dump(user)

    def serialize_user_data(self, user, fields=None):
        schema = self._get_user_schema()
        if fields:
            schema = UserSchema(many=True, exclude=fields)
        return schema.dump(user)
