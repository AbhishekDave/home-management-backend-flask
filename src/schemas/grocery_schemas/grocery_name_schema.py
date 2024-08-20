# src/schemas/grocery_schemas/grocery_name_schema.py

from marshmallow import Schema, fields, validate
from src.models.grocery_models.grocery_name_model import GroceryName


class GroceryNameSchema(Schema):
    class Meta:
        model = GroceryName

    id = fields.Integer(dump_only=True)     # Provided in output (e.g., responses)
    name = fields.String(required=True, validate=validate.Length(min=2, max=80))    # Provided in both Input and output (e.g., responses)
    grocery_type = fields.String(required=True, validate=validate.Length(min=2, max=80))
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
    is_active = fields.Boolean(dump_only=True)
    user_id = fields.Integer(dump_only=True)

    grocery_users = fields.Nested('UserSchema', only=("id", "first_name", "last_name"))        # type: ignore

    @staticmethod
    def get_grocery_users(obj):
        from src.schemas.auth_schemas.user_schema import UserSchema
        return UserSchema(many=True).dump(obj.grocery_users)

    @staticmethod
    def get_grocery_items(obj):
        from src.schemas.auth_schemas.user_schema import UserSchema
        return UserSchema(many=True).dump(obj.grocery_users)     # type: ignore


#   grocery_type_schema = GroceryNameSchema()
#   grocery_types_schema = GroceryNameSchema(many=True)
