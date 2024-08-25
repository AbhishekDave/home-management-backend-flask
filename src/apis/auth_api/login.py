# src/apis/auth_api/login.py

from flask import Blueprint, jsonify
from flask_jwt_extended import create_refresh_token, create_access_token
from src.decorators.auth_decorators.auth_requires_at_login import auth_requires_at_login, g
from src.decorators.unified_decorators.validate_request import validate_request
from src.schemas.auth_schemas.user_login_schema import UserLoginSchema

login_api_bp = Blueprint('login_api', __name__)


@login_api_bp.route('/login', methods=['POST'])
@validate_request('POST', schema_class=UserLoginSchema)
@auth_requires_at_login
def login():
    """
      API endpoint for user login.

      Returns:
          JSON response with success message, access token, and refresh token (if successful),
          or error message (if unsuccessful).
    """
    user = g.user  # Get the user object from the decorator

    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)

    return jsonify({'message': 'Login successful!', 'access_token': access_token, 'refresh_token': refresh_token})
