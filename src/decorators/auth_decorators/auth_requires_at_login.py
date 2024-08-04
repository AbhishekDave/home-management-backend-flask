# src/decorators/auth_decorators/auth_requires_at_login.py

from functools import wraps
from flask import request, jsonify, g
from src.models.auth_models.user_model import User


def auth_requires_at_login(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if request.method != 'POST':
            return jsonify({'message': 'Method not allowed.'}), 405

        data = request.get_json()
        if not data:
            return jsonify({'message': 'No input data provided.'}), 400

        credential = data.get('credential')
        password = data.get('password')

        if not credential or not password:
            return jsonify({'message': 'Missing credentials.'}), 400

        # Check if the credential is a username or email
        user = User.query.filter(
            (User.username == credential) | (User.email_id == credential)
        ).first()

        if not user or not user.check_password(password):  # if not user or not user.check_password(password):
            return jsonify({'message': 'Invalid credentials, please try again.'}), 401

        # Check if the user is active or not
        print(user.is_active)

        if not user.is_active:
            return jsonify({'message': 'Oops, User account does not activated, Please contact admin.'}), 401

        g.user = user  # Attach the user to the request for use in the view function

        return f(*args, **kwargs)

    return decorated
