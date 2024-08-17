# src/apis/auth_api/refresh.py

from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, create_access_token

from src.configs.development_config import db
from src.services.user_services import UserService

refresh_api_bp = Blueprint('refresh_api', __name__)


@refresh_api_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    user_service = UserService(db)
    current_user_id = user_service.find_current_user_id()
    new_access_token = create_access_token(identity=current_user_id)
    return jsonify(access_token=new_access_token)
