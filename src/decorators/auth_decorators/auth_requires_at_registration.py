# # src/decorators/auth_decorators/auth_requires_at_registration.py

from functools import wraps
from flask import request, jsonify
from src.models.auth_models.user_model import User


def auth_requires_at_registration(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        data = request.get_json()
        if not data:
            return jsonify({'message': 'No input data provided.'}), 400

        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'message': 'Required fields are missing. Please try again.'}), 400

        user_by_username = User.query.filter_by(username=username).first()

        if user_by_username:
            return jsonify({'message': 'User already exists.'}), 400

        return f(*args, **kwargs)

    return decorated

