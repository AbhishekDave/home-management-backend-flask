# src/schemas/grocery_schemas/store_schema.py
import re

from marshmallow import Schema, fields, validate, validates, ValidationError
from src.models.grocery_models.store_model import Store


class StoreSchema(Schema):
    class Meta:
        model = Store

    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=1, max=80))
    description = fields.String(allow_none=True, validate=validate.Length(max=255))
    location = fields.String(allow_none=True, validate=validate.Length(max=255))
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)

    # add nested schemas for relationships
    @property
    def products(self):
        from src.schemas.grocery_schemas.product_schema import ProductSchema
        return fields.List(fields.Nested(ProductSchema, many=True), dump_only=True)         # type: ignore

    @validates('name')
    def validate_name(self, value):
        if not value.strip():
            raise ValidationError("Name cannot be empty or just whitespace.")
        # Example: Ensure the name contains only alphabetic characters and spaces
        if not re.match(r'^[a-zA-Z\s]+$', value):
            raise ValidationError("Name must contain only alphabetic characters and spaces.")

    @validates('description')
    def validate_description(self, value):
        if value and len(value.split()) > 100:  # Example: Limit the description to a certain number of words
            raise ValidationError("Description is too verbose. Please keep it under 100 words.")
        # Example: Ensure the description does not contain any forbidden characters
        forbidden_chars = re.compile(r'[<>%$]')
        if forbidden_chars.search(value):
            raise ValidationError("Description contains forbidden characters like <, >, %, $.")

    @validates('location')
    def validate_location(self, value):
        # Example: Ensure the location is a valid format (e.g., address-like structure)
        if value:
            # Simple regex for address validation (can be more complex based on requirements)
            address_regex = re.compile(r'^[\w\s,.]+$')
            if not address_regex.match(value):
                raise ValidationError("Location format is invalid. Please use a valid address format.")


store_schema = StoreSchema()
stores_schema = StoreSchema(many=True)
