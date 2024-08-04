# src/schemas/grocery_schemas/store_schema.py

from marshmallow import Schema, fields, validate
from src.models.grocery_models.store_model import Store


class StoreSchema(Schema):
    class Meta:
        model = Store

    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=1, max=80))
    description = fields.String(allow_none=True)
    location = fields.String(allow_none=True)

    # add nested schemas for relationships
    @property
    def products(self):
        from src.schemas.grocery_schemas.product_schema import ProductSchema
        return fields.List(fields.Nested(ProductSchema, many=True), dump_only=True)


store_schema = StoreSchema()
stores_schema = StoreSchema(many=True)
