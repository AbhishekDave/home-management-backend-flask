# src/schemas/grocery_schemas/product_schema.py

from marshmallow import Schema, fields, validate
from src.models.grocery_models.product_model import Product


class ProductSchema(Schema):
    class Meta:
        model = Product

    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=1, max=80))
    product_type = fields.String(required=True, validate=validate.Length(min=1, max=80))
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)

    grocery_names = fields.List(fields.Nested('GroceryNameSchema', only=("id", "name", "grocery_type")), dump_only=True)        # type: ignore

    stores = fields.List(fields.Nested('Store', only=("id", "name", "description", "location")), dump_only=True)            # type: ignore
