# src/apis/auth_api/logout.py

from flask import jsonify, Blueprint
from flask_jwt_extended import jwt_required, get_jwt
from src.configs.development_config import ACCESS_EXPIRES_HOURS, ACCESS_EXPIRES_MINUTES, redis_client, \
    CURRENT_TIME_AT_TIMEZONE

logout_api_bp = Blueprint('logout_api', __name__)


@logout_api_bp.route('/logout', methods=['DELETE'])
@jwt_required()
def logout():
    token = get_jwt()
    jti = token["jti"]
    ttype = token["type"]

    # Blacklist the token
    expiration_time = CURRENT_TIME_AT_TIMEZONE + ACCESS_EXPIRES_MINUTES
    redis_client.setex(jti, int(expiration_time.timestamp()), ttype)

    return jsonify(msg=f"Logout Successfully with {ttype.capitalize()} token successfully blacklisted."), 200
