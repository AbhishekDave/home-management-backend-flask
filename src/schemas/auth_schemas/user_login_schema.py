# src/schemas/auth_schemas/user_schema.py
import re

from marshmallow import Schema, ValidationError, fields, validate, validates
from src.models.auth_models.user_model import User


class UserLoginSchema(Schema):
    class Meta:
        model = User

    # username field either be a username or email
    username = fields.String(required=True,
                             validate=validate.Length(min=3))  # Provided in both input and output

    password = fields.String(required=True, load_only=True,
                             validate=validate.Length(min=6))  # Sensitive data; only for input

    is_active = fields.Boolean(dump_only=True, default=True)  # Provided in output

    last_login = fields.DateTime(dump_only=True)  # Provided in output

    created_at = fields.DateTime(dump_only=True)  # Provided in output

    modified_at = fields.DateTime(dump_only=True)  # Provided in output

    @validates('username')
    def validate_username(self, value):
        if not self._is_valid_email(value) and not self._is_valid_username(value):
            raise ValidationError("Please enter a valid username or email for login.")

    @staticmethod
    def _is_valid_email(value):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?$'
        return re.match(email_regex, value)

    @staticmethod
    def _is_valid_username(value):
        return re.match(r'^[a-zA-Z0-9_-]+$', value) and re.match(r'^[a-zA-Z]', value)

    @validates('password')
    def validate_password(self, value):
        if len(value) < 6:
            raise ValidationError("Password must be at least 6 characters long.")
