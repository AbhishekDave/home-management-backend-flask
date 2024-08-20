# src/apis/grocery_api/grocery_api_get.py

from flask import Blueprint, request, current_app, jsonify
from flask_jwt_extended import jwt_required

from src.configs.development_config import db

from src.services.user_services import UserService
from src.services.grocery_services import GroceryService
from src.services.serialization_services.grocery_serialization_service import GrocerySerializationService

grocery_name_get_api_bp = Blueprint('grocery_name_get_api', __name__)


@grocery_name_get_api_bp.route('/grocery-names', methods=['GET'])
@jwt_required()
def get_grocery_names():
    # Log the incoming request URL
    api_url = request.url
    current_app.logger.info(f"\nRequest URL: {api_url}")

    user_service = UserService(db)
    grocery_service = GroceryService(db)
    grocery_serialization_service = GrocerySerializationService()

    current_user_id = user_service.find_current_user_id()

    grocery_name_list = grocery_service.find_all_grocery_names_by_user_id(current_user_id)

    fields_to_exclude = []
    grocery_data_dump = grocery_serialization_service.serialize_grocery_names(grocery_name_list, fields=fields_to_exclude)

    return jsonify(grocery_data_dump)
