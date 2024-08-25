# src/apis/auth_api/reset_password.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from src.configs.development_config import db, REDIS_CLIENT
from src.services.auth_services import AuthServices

from src.utils import TokenUnauthorizedException

reset_password_api_bp = Blueprint('reset_password_api', __name__)


@reset_password_api_bp.route('/reset-password', methods=['POST'])
@jwt_required()
def reset_password():
    data = request.get_json()
    if not data or 'token' not in data or 'new_password' not in data:
        return jsonify({"message": "Token and new password are required."}), 400

    token = data['token']
    new_password = data['new_password']

    auth_services = AuthServices(db)

    try:
        decoded_data = auth_services.validate_forgot_password_token(token)

        stored_username_or_email = REDIS_CLIENT.get(f"forgot_password_token:{token}")
        if not stored_username_or_email:
            raise TokenUnauthorizedException('Invalid or expired token.')

        auth_services.user_service.update_new_password(stored_username_or_email, new_password)

        REDIS_CLIENT.delete(f"forgot_password_token:{token}")

        return jsonify({"message": "Password reset successfully."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 400
