# src/apis/auth_api/register.py

from flask import jsonify, Blueprint
from flask_jwt_extended import create_access_token, create_refresh_token

from src.configs.development_config import db

from src.services.user_services import UserService
from src.services.serialization_services.user_serialization_service import UserSerializationService
from src.schemas.auth_schemas.user_registration_schema import UserRegistrationSchema

from src.decorators.auth_decorators.auth_requires_at_registration import auth_requires_at_registration
from src.decorators.unified_decorators.validate_request import validate_request, g

register_api_bp = Blueprint('register_api', __name__)


@register_api_bp.route('/register', methods=['POST'])
@validate_request('POST', schema_class=UserRegistrationSchema)
@auth_requires_at_registration
def register():

    user_service = UserService(db)
    user_serialization_service = UserSerializationService()

    user_data = g.validated_data

    try:
        new_user = user_service.create_user(user_data)
    except ValueError as e:
        return jsonify({'message': str(e)}), 400

    # Create response (excluding password)
    user_data_dump = user_serialization_service.serialize_user_registration_data(new_user)
    access_token = create_access_token(identity=new_user.id)
    refresh_token = create_refresh_token(identity=new_user.id)

    # Created and Excluded password from response because of @post_dump
    return jsonify(message="User created successfully", access_token=access_token, refresh_token=refresh_token, user=user_data_dump), 201
