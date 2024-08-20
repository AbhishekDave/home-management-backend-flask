# src/services/serialization_services/grocery_serialization.py

from src.schemas.grocery_schemas.grocery_name_schema import GroceryNameSchema


class GrocerySerializationService:
    def __init__(self):
        self.grocery_name_schema = self._get_grocery_name_schema()
        self.grocery_names_schema = self._get_grocery_names_schema()

    @staticmethod
    def _get_grocery_name_schema():
        from src.schemas.grocery_schemas.grocery_name_schema import GroceryNameSchema
        return GroceryNameSchema()

    @staticmethod
    def _get_grocery_names_schema():
        from src.schemas.grocery_schemas.grocery_name_schema import GroceryNameSchema
        return GroceryNameSchema(many=True)

    def serialize_grocery_names(self, grocery_name_list, fields=None):
        schema = self._get_grocery_names_schema()
        if fields:
            schema = GroceryNameSchema(many=True, exclude=fields)
        return schema.dump(grocery_name_list)
