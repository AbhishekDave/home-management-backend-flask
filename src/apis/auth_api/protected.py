# src/apis/auth_api/protected.py

from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

from src.configs.development_config import db
from src.services.user_services import UserService
from src.utils.error_handling_utility.exceptions import InternalServerException

protected_api_bp = Blueprint('protected_api', __name__)


@protected_api_bp.route('/protected', methods=['GET'])
@jwt_required()  # Adjust based on your needs; remove verify_type if not needed
def protected():
    """
    Access a protected resource.

    Requires a valid JWT access token. Returns the identity of the currently authenticated user.

    Returns:
        JSON response with the username of the currently logged-in user and a 200 status code.
    """
    user_Service = UserService(db)
    try:
        # Retrieve the identity of the current user
        current_user_id = user_Service.find_current_user_id()

        # Return a JSON response with user information
        return jsonify(logged_in_as=current_user_id), 200

    except InternalServerException:

        # Raise an exception with appropriate error response
        raise InternalServerException('An error occurred while processing the request.')
