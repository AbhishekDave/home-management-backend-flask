# src/schemas/auth_schemas/user_schema.py

from marshmallow import Schema, ValidationError, fields, pre_load, post_dump, validate
from src.models.auth_models.user_model import User


class UserSchema(Schema):
    class Meta:
        model = User

    id = fields.Integer(dump_only=True)  # Provided in output (e.g., responses)
    first_name = fields.String(required=True)  # Provided in both input and output
    last_name = fields.String(required=True)  # Provided in both input and output
    username = fields.String(required=True, validate=validate.Length(min=3, max=30))  # Provided in both input and output
    password = fields.String(required=True, load_only=True, validate=validate.Length(min=6))  # Sensitive data; only for input
    email_id = fields.Email(required=True)  # Provided in both input and output
    address = fields.String(load_only=True, missing='Not Provided')  # Sensitive data; only for input
    phone = fields.String(allow_none=True, load_only=True)  # Sensitive data; only for input
    is_active = fields.Boolean(dump_only=True, default=True)  # Provided in output
    created_at = fields.DateTime(dump_only=True)  # Provided in output

    @post_dump(pass_many=False)
    def remove_password(self, data, **kwargs):
        data.pop('id', None)                        # eliminating in response
        data.pop('password', None)                  # eliminating in response
        data.pop('created_at', None)
        return data


user_schema = UserSchema()
users_schema = UserSchema(many=True)
