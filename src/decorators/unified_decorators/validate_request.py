# src/decorators/unified_decorators/validate_requests

from functools import wraps
from flask import request, jsonify, g
from marshmallow import ValidationError

from src.utils.exceptions import MethodNotAllowedException, UnsupportedMediaTypeException, MissingDataException


def validate_request(method, schema=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # Check if the request method matches the specified method
            if request.method != method:
                raise MethodNotAllowedException('Method not allowed.')

            # Check Content-Type
            if request.content_type != 'application/json':
                raise UnsupportedMediaTypeException('Content-Type must be application/json.')

            # Check if JSON data is provided
            data = request.get_json()
            if not data:
                raise MissingDataException('No input data provided.')

            # Validate data using Marshmallow schema if provided
            if schema:
                try:
                    validated_data = schema.load(data)
                except ValidationError as err:
                    return jsonify(err.messages), 400
                # Add validated data to kwargs
                g.validated_data = validated_data

            return f(*args, **kwargs)
        return decorated_function
    return decorator
