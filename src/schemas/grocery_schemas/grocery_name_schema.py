# src/schemas/grocery_schemas/grocery_name_schema.py

from marshmallow import Schema, fields, validate
from src.models.grocery_models.grocery_name_model import GroceryName


class GroceryNameSchema(Schema):
    class Meta:
        model = GroceryName

    id = fields.Integer(dump_only=True)     # Provided in output (e.g., responses)
    name = fields.String(required=True, validate=validate.Length(min=2, max=80))    # Provided in both Input and output (e.g., responses)
    type = fields.String(required=True, validate=validate.Length(min=2, max=80))
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
    is_active = fields.Boolean(dump_only=True)
    user_id = fields.Integer(dump_only=True)

    # Use lazy loading by passing the schema class names as strings
    # users = fields.List(fields.Nested('CompleteUserSchema'), dump_only=True)
    # grocery_items = fields.List(fields.Nested('GroceryItemSchema'), dump_only=True)

    # nested schemas for relationships
    @property
    def users(self):
        from src.schemas.auth_schemas.complete_user_schema import CompleteUserSchema
        return fields.List(fields.Nested(CompleteUserSchema, many=True), dump_only=True)     # type: ignore

    @property
    def grocery_items(self):
        from src.schemas.grocery_schemas.grocery_item_schema import GroceryItemSchema
        return fields.List(fields.Nested(GroceryItemSchema, many=True), dump_only=True)     # type: ignore


grocery_type_schema = GroceryNameSchema()
grocery_types_schema = GroceryNameSchema(many=True)
