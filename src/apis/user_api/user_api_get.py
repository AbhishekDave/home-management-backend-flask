# src/apis/grocery_api/user_api_get.py

from flask import Blueprint, request, current_app, jsonify
from flask_jwt_extended import jwt_required

from src.configs.development_config import db
from src.services import UserSerializationService

from src.services.user_services import UserService

"""from flask_injector import inject"""

user_api_get_bp = Blueprint('user_api_get_bp', __name__)


@user_api_get_bp.route('/users/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user():
    # Log the incoming URL requests
    api_url = request.url
    current_app.logger.info(f'Request url: {api_url}')

    return None


@user_api_get_bp.route('/user/grocery-name-lists', methods=['GET'])
@jwt_required()
def get_user_with_grocery_name_lists():
    # Log the incoming URL requests
    api_url = request.url
    current_app.logger.info(f'Request url: {api_url}')

    user_service = UserService(db)
    user_serialization_service = UserSerializationService()

    current_user_id = user_service.find_current_user_id()

    user_with_grocery_list = user_service.find_user_with_groceries(current_user_id)

    fields_to_exclude = []

    user_with_grocery_lists_dump = user_serialization_service.serialize_user_data(user_with_grocery_list, fields_to_exclude)

    return jsonify(user_with_grocery_lists_dump)


@user_api_get_bp.route('/user/grocery-names-lists', methods=['GET'])
@jwt_required()
def get_user_with_a_grocery_name_lists():
    # Log the incoming URL requests
    api_url = request.url
    current_app.logger.info(f'Request url: {api_url}')

    user_service = UserService(db)
    user_serialization_service = UserSerializationService()

    current_user_id = user_service.find_current_user_id()
    user_with_grocery_list = user_service.find_user_with_groceries(current_user_id)
    user_with_grocery_lists_dump = user_serialization_service.serialize_user_data(user_with_grocery_list)

    return jsonify(user_with_grocery_lists_dump)


"""@user_api_get_bp.route('/user/grocery-name-lists', methods=['GET'])
@jwt_required()
@inject
def get_user_with_grocery_names_lists(user_service: UserService, user_serialization_service: UserSerializationService):
    api_url = request.url
    current_app.logger.info(f'Request url: {api_url}')

    current_user_id = user_service.find_current_user_id()
    user_with_grocery_list = user_service.find_user_with_groceries(current_user_id)
    user_with_grocery_lists_dump = user_serialization_service.dump_user_schema(user_with_grocery_list)

    return jsonify(user_with_grocery_lists_dump)"""
