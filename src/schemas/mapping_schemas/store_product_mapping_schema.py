# src/schemas/mapping_schemas/store_product_name_schema.py

from marshmallow import Schema, fields, validates, ValidationError

from src.models.mapping_models.store_product_mapping_model import StoreProductMapping


class StoreProductMappingSchema(Schema):
    class Meta:
        model = StoreProductMapping

        id = fields.Integer(dump_only=True)
        store_id = fields.Integer(dump_only=True)
        product_id = fields.Integer(dump_only=True)
        price = fields.Integer(dump_only=True)
        quantity = fields.Integer(dump_only=True)
        expiry_date = fields.DateTime(dump_only=True)
        created_at = fields.DateTime(dump_only=True)
        modified_at = fields.DateTime(dump_only=True)

    @validates('price')
    def validate_price(self, price):
        if price <= 0:
            raise ValidationError('Price must be greater than 0')

    @validates('quantity')
    def validate_quantity(self, quantity):
        if quantity <= 0:
            raise ValidationError('Quantity must be greater than 0')

    @validates('expiry_date')
    def validate_expiry_date(self, expiry_date):
        from datetime import datetime
        if expiry_date is None:
            raise ValidationError('Expiry_date cannot be None')
        elif expiry_date <= datetime.now().date():
            raise ValidationError('Expiry_date must be today or in the future')
