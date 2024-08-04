# src/schemas/user_schema.py

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields, post_dump
from src.models.auth_models.user_model import User


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User

    id = fields.Integer(dump_only=True)
    first_name = fields.String(dump_only=True)
    last_name = fields.String(dump_only=True)
    username = fields.String(required=True)
    password = fields.String(required=True, load_only=True)  # Don't expose in response
    email_id = fields.Email(required=True)
    address = fields.String(required=True, load_only=True)  # Don't expose in response
    phone = fields.String(required=True, load_only=True)    # Don't expose in response
    is_active = fields.Boolean(dump_only=True)              # Don't expose in response
    created_at = fields.DateTime(dump_only=True)

    @post_dump(pass_many=False)
    def remove_password(self, data, **kwargs):
        data.pop('id', None)                        # eliminating in response
        data.pop('password', None)                  # eliminating in response
        data.pop('created_at', None)
        return data


user_schema = UserSchema()
users_schema = UserSchema(many=True)
