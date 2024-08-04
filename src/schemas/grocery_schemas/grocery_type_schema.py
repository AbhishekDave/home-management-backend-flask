# src/schemas/grocery_schemas/grocery_type_schema.py

from marshmallow import Schema, fields, validate
from src.models.grocery_models.grocery_type_model import GroceryType


class GroceryTypeSchema(Schema):
    class Meta:
        model = GroceryType

    id = fields.Integer(dump_only=True)     # Provided in output (e.g., responses)
    name = fields.String(required=True, validate=validate.Length(min=1, max=80))    # Provided in both Input and output (e.g., responses)

    # add nested schemas for relationships
    @property
    def products(self):
        from src.schemas.grocery_schemas.product_schema import ProductSchema
        return fields.List(fields.Nested(ProductSchema, many=True), dump_only=True)     # Provided in output (e.g., responses)


grocery_type_schema = GroceryTypeSchema()
grocery_types_schema = GroceryTypeSchema(many=True)
