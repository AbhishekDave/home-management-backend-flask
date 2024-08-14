# src/schemas/grocery_schemas/product_schema.py

from datetime import datetime
from marshmallow import Schema, fields, validate
from src.models.grocery_models.grocery_item_model import GroceryItem


class ProductSchema(Schema):
    class Meta:
        model = GroceryItem

    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=1, max=80))
    type = fields.String(required=True, validate=validate.Length(min=1, max=80))
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)

    # add nested schemas for relationships
    @property
    def grocery_type(self):
        from src.schemas.grocery_schemas.grocery_name_schema import GroceryNameSchema
        return fields.Nested(GroceryNameSchema, dump_only=True)

    @property
    def store(self):
        from src.schemas.grocery_schemas.store_schema import StoreSchema
        return fields.Nested(StoreSchema, dump_only=True)


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
