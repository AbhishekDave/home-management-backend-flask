# src/apis/auth_api/registration.py

from flask import request, jsonify, Blueprint
from flask_jwt_extended import create_access_token, create_refresh_token
from src.configs.development_config import db
from src.decorators.auth_decorators.auth_requires_at_registration import auth_requires_at_registration
from src.models.user_model import User
from src.schemas.user_schema import UserSchema

register_api_bp = Blueprint('register_api', __name__)


@register_api_bp.route('/register', methods=['POST'])
@auth_requires_at_registration
def register():
    # Get data from request
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user_schema = UserSchema()

    new_user = User(username=username)
    new_user.set_password(password)

    # Save user to database
    db.session.add(new_user)
    db.session.commit()

    # Create response (excluding password)
    user_data = user_schema.dump(new_user)
    access_token = create_access_token(identity=new_user.id)
    refresh_token = create_refresh_token(identity=new_user.id)

    # Created and Excluded password from response because of @post_dump
    return jsonify(message="User created successfully", access_token=access_token, refresh_token=refresh_token, user=user_data), 201


