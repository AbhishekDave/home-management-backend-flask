# src/schemas/grocery_schemas/grocery_item_schema.py

from marshmallow import Schema, fields
from src.models.grocery_models.grocery_item_model import GroceryItem


class GroceryItemSchema(Schema):
    class Meta:
        model = GroceryItem

        id = fields.Integer(dump_only=True)
        grocery_name_id = fields.Integer(dump_only=True)
        item_id = fields.Integer(dump_only=True)
        created_at = fields.DateTime(dump_only=True)
        modified_at = fields.DateTime(dump_only=True)

        @property
        def items(self):
            from src.schemas.grocery_schemas.grocery_name_schema import GroceryNameSchema
            return fields.List(fields.Nested(GroceryNameSchema), dump_only=True)


grocery_item_schema = GroceryItemSchema()
grocery_items_schema = GroceryItemSchema(many=True)
