# src/services/grocery_services.py

from src.services.user_services import UserService
from src.repositories.grocery_repository import GroceryRepository, GroceryName
from src.utils.error_handling_utility.exceptions import ConflictException, NotFoundException


class GroceryService:
    def __init__(self, db):
        self.grocery_repository = GroceryRepository(db)
        self.grocery_name = GroceryName()
        self.user_service = UserService(db)

    # CREATE Operations
    def create_grocery(self, grocery_name_data):
        """
        Creates a new grocery_name and saves it to the database.

        :param grocery_name_data: Dictionary containing grocery name information.
        :return: The created grocery name object by current logged-in user.
        """
        current_user_id = self.user_service.find_current_user_id()
        new_grocery_name = GroceryName(**grocery_name_data)
        new_grocery_name.user_id = current_user_id

        # Check if the grocery name already exists for the user
        existing_grocery_name = self.find_grocery_name_by_user_and_name(current_user_id, grocery_name_data['name'])
        if existing_grocery_name is not None:
            raise ConflictException(f"Grocery Name '{existing_grocery_name.name}' already exists.")

        try:
            self.grocery_repository.add_grocery_name(new_grocery_name)

        except Exception as e:
            # Handle database errors (e.g., duplicate names, connection issues)
            raise ValueError(f"An error occurred while saving the grocery name: {str(e)}")

        return new_grocery_name

    def find_grocery_name_by_user_and_name(self, user_id, grocery_name):
        """
        Searches the database for unique pair of grocery name and user and returns it.
        :param user_id: User ID.
        :param grocery_name: Grocery name.
        :return: Grocery name object by current logged-in user.
        """
        grocery_name_by_user_and_name = self.grocery_repository.get_grocery_name_by_user_and_name(user_id, grocery_name)
        return grocery_name_by_user_and_name

    def find_all_grocery_names_by_user_id(self, user_id):
        """
        Searches the database for list of all the grocery name associated with specific user and returns it.
        :param user_id: User ID.
        :return: List of Grocery names object by current logged-in user.
        """
        grocery_name_list = self.grocery_repository.get_all_grocery_names_by_user(user_id)
        if not grocery_name_list:
            raise NotFoundException(f"No grocery names found for user_id: {user_id}")

        return grocery_name_list
