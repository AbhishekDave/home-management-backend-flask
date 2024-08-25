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

        item_in_groceries = fields.Nested('GroceryItemSchema', dump_only=True)          # type: ignore
