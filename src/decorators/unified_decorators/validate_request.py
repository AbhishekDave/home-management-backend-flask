# src/decorators/unified_decorators/validate_requests

from functools import wraps
from flask import request, jsonify, g
from marshmallow import ValidationError

from src.utils.error_handling_utility.exceptions import MethodNotAllowedException, UnsupportedMediaTypeException, MissingDataException


def validate_request(method, schema_class=None):
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

            # Validate data using Marshmallow schema for multiple or single object on provided
            if schema_class:
                try:
                    # Create an instance of the schema class
                    if isinstance(data, list):
                        # Validate as a list of objects
                        schema = schema_class(many=True)
                    else:
                        # Validate as a single object
                        schema = schema_class()

                    # Load and validated
                    validated_data = schema.load(data)
                    # Add validated data to g for global access
                    g.validated_data = validated_data
                except ValidationError as err:
                    return jsonify(err.messages), 400

            return f(*args, **kwargs)
        return decorated_function
    return decorator
