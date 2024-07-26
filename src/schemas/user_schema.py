# src/schemas/user_schema.py

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields, post_dump
from src.models.user_model import User


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User

    id = fields.Integer(dump_only=True)
    username = fields.String(required=True)
    password = fields.String(required=True, load_only=True)  # Don't expose password in response

    @post_dump(pass_many=False)
    def remove_password(self, data, **kwargs):
        data.pop('id', None)                        # eliminating user_id in response
        data.pop('password', None)                  # eliminating password in response
        return data


user_schema = UserSchema()
users_schema = UserSchema(many=True)
