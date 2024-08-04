# src/schemas/grocery_schemas/product_schema.py

from marshmallow import Schema, fields, validate
from src.models.grocery_models.product_model import Product


class ProductSchema(Schema):
    class Meta:
        model = Product

    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=1, max=80))
    price = fields.Float(required=True)
    product_type = fields.String(required=True, validate=validate.Length(min=1, max=80))
    expiry_date = fields.Date(required=True)
    grocery_type_id = fields.Integer(required=True)
    store_id = fields.Integer(required=True)

    # add nested schemas for relationships
    @property
    def grocery_type(self):
        from src.schemas.grocery_schemas.grocery_type_schema import GroceryTypeSchema
        return fields.Nested(GroceryTypeSchema, dump_only=True)

    @property
    def store(self):
        from src.schemas.grocery_schemas.store_schema import StoreSchema
        return fields.Nested(StoreSchema, dump_only=True)


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

