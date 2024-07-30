from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

protected_api_bp = Blueprint('protected_api', __name__)


@protected_api_bp.route('/protected', methods=['GET'])
@jwt_required(verify_type=True)
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
