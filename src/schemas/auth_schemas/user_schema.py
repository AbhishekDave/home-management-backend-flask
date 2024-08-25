# src/schemas/auth_schemas/user_schema.py

import re

from marshmallow import Schema, ValidationError, fields, validate, validates
from src.models.auth_models.user_model import User


class UserSchema(Schema):
    class Meta:
        model = User

    id = fields.Integer(dump_only=True)  # Provided in output (e.g., responses)
    first_name = fields.String(required=True,
                               validate=validate.Length(min=1, max=50))  # Provided in both input and output

    last_name = fields.String(required=True,
                              validate=validate.Length(min=1, max=50))  # Provided in both input and output

    username = fields.String(required=True,
                             validate=validate.Length(min=3, max=20))  # Provided in both input and output

    password = fields.String(required=True, load_only=True,
                             validate=validate.Length(min=6))  # Sensitive data; only for input

    email = fields.Email(required=True)  # Provided in both input and output

    address = fields.String(load_only=True,
                            validate=validate.Length(min=200))  # Sensitive data; only for input

    phone = fields.String(allow_none=True, load_only=True,
                          validate=validate.Length(min=10, max=15))  # Sensitive data; only for input

    is_active = fields.Boolean(dump_only=True, default=True)  # Provided in output

    last_login = fields.DateTime(dump_only=True)  # Provided in output

    created_at = fields.DateTime(dump_only=True)  # Provided in output

    modified_at = fields.DateTime(dump_only=True)  # Provided in output

    user_groceries = fields.List(fields.Nested('GroceryNameSchema', only=("id", "name", "grocery_type")), dump_only=True)                # type: ignore

    @validates('username')
    def validate_username(self, value):
        # Example custom validation for username
        # Check for alphanumeric characters, underscores, or hyphens
        if not re.match(r'^[a-zA-Z0-9_-]+$', value):
            raise ValidationError("Username must be alphanumeric, underscores, or hyphens.")
        # Check if username starts with a letter if that's a requirement
        if not re.match(r'^[a-zA-Z]', value):
            raise ValidationError("Username must start with a letter.")

    @validates('password')
    def validate_password(self, value):
        # Example custom validation for password
        if len(value) < 6:
            raise ValidationError("Password must be at least 6 characters long.")
        # You can add more complex password validation here if needed

    @validates('email')
    def validate_email(self, value):
        # Define a regex pattern for a valid email address
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?$'
        if not re.match(email_regex, value):
            raise ValidationError("Invalid email format.")
