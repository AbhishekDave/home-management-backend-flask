# src/apis/auth_api/login.py

from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

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
    try:
        # Retrieve the identity of the current user
        current_user = get_jwt_identity()

        # Return a JSON response with user information
        return jsonify(logged_in_as=current_user), 200

    except Exception as e:

        # Return an appropriate error response
        return jsonify(message="An error occurred while processing the request.", error=str(e)), 500
