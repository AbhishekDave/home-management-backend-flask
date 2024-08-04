# src/schemas/mapping_schemas/user_grocery_type_schema.py

from marshmallow import Schema, fields
from src.models.mapping_models.user_grocery_type_model import UserGroceryType


class UserGroceryTypeSchema(Schema):
    class Meta:
        model = UserGroceryType

    id = fields.Integer(dump_only=True)
    user_id = fields.Integer(required=True)
    grocery_type_id = fields.Integer(required=True)

    # Add nested schemas for relationships

    @property
    def user(self):
        from src.schemas.auth_schemas.user_schema import UserSchema
        return fields.Nested(UserSchema, dump_only=True)

    @property
    def grocery_type(self):
        from src.schemas.grocery_schemas.grocery_type_schema import GroceryTypeSchema
        return fields.Nested(GroceryTypeSchema, dump_only=True)


user_grocery_type_schema = UserGroceryTypeSchema()
user_grocery_types_schema = UserGroceryTypeSchema(many=True)

