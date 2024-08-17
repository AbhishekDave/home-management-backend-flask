# src/services/serialization_services/grocery_serialization.py

from src.schemas.grocery_schemas.grocery_name_schema import GroceryNameSchema


class GrocerySerializationService:
    def __init__(self):
        self.grocery_name_schema = GroceryNameSchema()
        self.grocery_names_schema = GroceryNameSchema(many=True)

    def dump_grocery_name_schema(self, grocery_name_data):
        return self.grocery_name_schema.dump(grocery_name_data)

    def serialize_grocery_names(self, grocery_name_list):
        """
        Serialize a list of grocery names.
        :param grocery_name_list:
        :return: Serialized data as per GroceryNameSchema.
        """
        return self.grocery_names_schema.dump(grocery_name_list)
