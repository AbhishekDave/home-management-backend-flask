# src/apis/auth_api/forgot_password.py

from flask import Blueprint, request, jsonify

from src.configs.development_config import REDIS_CLIENT, ACCESS_EXPIRES_IN_5_MIN, db
from src.decorators.auth_decorators.auth_requires_at_forgot_password import auth_requires_at_forgot_password, g
from src.services.auth_services import AuthServices
from src.utils import NotFoundException

forgot_password_api_bp = Blueprint('forgot_password_api', __name__)


@forgot_password_api_bp.route('/forgot-password', methods=['POST'])
@auth_requires_at_forgot_password
def forgot_password():
    username_or_email = g.user_data

    auth_services = AuthServices(db)

    try:
        token = auth_services.create_forgot_password_token(username_or_email)

        REDIS_CLIENT.setex(f"forgot_password_token:{token}", ACCESS_EXPIRES_IN_5_MIN, username_or_email)

        return jsonify({"message": "Reset token generated.", "token": token}), 200
    except NotFoundException as e:
        return jsonify({"message": str(e)}), 404
