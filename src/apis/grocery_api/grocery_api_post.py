# src/apis/grocery_api/grocery_api_post.py

from flask import Blueprint, request, current_app, jsonify
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import SQLAlchemyError

from src.configs.development_config import db
from src.utils.error_handling_utility.exceptions import InternalServerException
from src.decorators.unified_decorators.validate_request import validate_request, g

from src.schemas.grocery_schemas.grocery_name_schema import GroceryNameSchema

from src.services.user_services import UserService
from src.services.grocery_services import GroceryService
from src.services.serialization_services.grocery_serialization_service import GrocerySerializationService

grocery_name_post_api_bp = Blueprint('grocery_name_post_api', __name__)


@grocery_name_post_api_bp.route('/grocery-name', methods=['POST'])
@jwt_required()
@validate_request('POST', schema_class=GroceryNameSchema)
def add_grocery_name(**kwargs):
    # Log the incoming request URL
    api_url = request.url
    current_app.logger.info(f"\nRequest URL: {api_url}")

    user_service = UserService(db)
    grocery_service = GroceryService(db)
    grocery_serialization_service = GrocerySerializationService()

    current_user_id = user_service.find_current_user_id()

    grocery_name_data = g.validated_data

    created_grocery_names = []

    try:
        if isinstance(grocery_name_data, list):
            for grocery_name in grocery_name_data:
                new_grocery_name = grocery_service.create_grocery(grocery_name)
                current_app.logger.info(f"\nAdded Grocery Name Data: {new_grocery_name.name} \nAdded by user: {current_user_id}")
                created_grocery_names.append(new_grocery_name)
        else:
            new_grocery_name = grocery_service.create_grocery(grocery_name_data)
            current_app.logger.info(f"\nAdded Grocery Name Data: {new_grocery_name.name} \nAdded by user: {current_user_id}")
            created_grocery_names.append(new_grocery_name)

        fields_to_exclude = []
        grocery_data_dump = grocery_serialization_service.serialize_grocery_names(created_grocery_names, fields=fields_to_exclude)

    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback the session in case of an error
        current_app.logger.error(f"\nDatabase error occurred: {e}")
        raise InternalServerException('Database error occurred')

    return jsonify(message="Grocery Name added successfully", grocery_name_data=grocery_data_dump), 201
