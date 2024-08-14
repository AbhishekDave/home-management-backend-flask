from zoneinfo import ZoneInfo

from flask import jsonify
from datetime import datetime
from src.utils.error_handling_utility.exceptions import (
    MissingDataException, MissingCredentialsException, CredentialsUnauthorizedException,
    MethodNotAllowedException, NotFoundException, ConflictException, TokenUnauthorizedException,
    UnprocessableEntityException, PreconditionFailedException, GatewayTimeoutException, InternalServerException,
    BadRequestException, UnsupportedMediaTypeException
)


class ErrorHandlers:
    @staticmethod
    def handle_missing_data_exception(e):
        """
        Handles MissingDataException.
        Use this handler for cases where required input data is missing.
        """
        return jsonify({
            'message': 'No input data provided.',
            'error': 'Missing Data Exception: ' + str(e),
            'error_code': '4001',
            'timestamp': datetime.now(ZoneInfo('UTC'))
        }), 400

    @staticmethod
    def handle_missing_credentials_exception(e):
        """
        Handles MissingCredentialsException.
        Use this handler for cases where credentials are missing from the request.
        """
        return jsonify({
            'message': 'Missing credentials.',
            'error': 'Missing Credentials Exception: ' + str(e),
            'error_code': '4002',
            'timestamp': datetime.now(ZoneInfo('UTC'))
        }), 400

    @staticmethod
    def handle_bad_request_error(e):
        """
        Handles general bad request errors.
        Use this handler for any other general 400 errors not covered by specific exceptions.
        """
        return jsonify({
            'message': 'Bad request.',
            'error': 'Bad Request Exception: ' + str(e),
            'error_code': '4003',
            'timestamp': datetime.now(ZoneInfo('UTC'))
        }), 400

    @staticmethod
    def handle_custom_unauthorized_exception(e):
        """
        Handles CustomUnauthorizedException.
        Use this handler for unauthorized access due to invalid credentials or inactive accounts.
        """
        return jsonify({
            'message': 'Unauthorized: Invalid credentials or inactive account.',
            'error': 'Unauthorized Exception: ' + str(e),
            'error_code': '4011',
            'timestamp': datetime.now(ZoneInfo('UTC'))
        }), 401

    @staticmethod
    def handle_unauthorized_token_error(e):
        """
        Handles general unauthorized token errors.
        Use this handler for token-related issues or other unauthorized access errors.
        """
        return jsonify({
            'message': 'Unauthorized: Token expired or invalid token.',
            'error': 'Unauthorized Error: ' + str(e),
            'error_code': '4012',
            'timestamp': datetime.now(ZoneInfo('UTC'))
        }), 401

    @staticmethod
    def handle_method_not_allowed_exception(e):
        """
        Handles MethodNotAllowedException.
        Use this handler when a method is not allowed for the requested URL.
        """
        return jsonify({
            'message': 'Method not allowed.',
            'error': 'Method Not Allowed Exception: ' + str(e),
            'error_code': '4051',
            'timestamp': datetime.now(ZoneInfo('UTC'))
        }), 405

    @staticmethod
    def handle_internal_server_error(e):
        """
        Handles generic internal server errors.
        Use this handler for any other 500 errors not covered by specific exceptions.
        """
        return jsonify({
            'message': 'Internal server error.',
            'error': 'Internal Server Error Exception: ' + str(e),
            'error_code': '5001',
            'timestamp': datetime.now(ZoneInfo('UTC'))
        }), 500

    @staticmethod
    def handle_not_found_exception(e):
        """
        Handles NotFoundException.
        Use this handler for cases where a requested resource is not found.
        """
        return jsonify({
            'message': 'Resource not found.',
            'error': 'Not Found Exception: ' + str(e),
            'error_code': '4041',
            'timestamp': datetime.now(ZoneInfo('UTC'))
        }), 404

    @staticmethod
    def handle_conflict_exception(e):
        """
        Handles ConflictException.
        Use this handler for cases where there is a conflict with the current state of the resource,
        such as when trying to create a resource with a unique constraint violation (e.g., username already exists).
        """
        return jsonify({
            'message': 'Conflict occurred.',
            'error': 'Conflict Exception: ' + str(e),
            'error_code': '4091',
            'timestamp': datetime.now(ZoneInfo('UTC'))
        }), 409

    @staticmethod
    def handle_unprocessable_entity_exception(e):
        """
        Handles UnprocessableEntityException.
        Use this handler for cases where the request is well-formed but cannot be processed due to semantic errors.
        """
        return jsonify({
            'message': 'Unprocessable entity.',
            'error': 'Unprocessable Entity Exception: ' + str(e),
            'error_code': '4221',
            'timestamp': datetime.now(ZoneInfo('UTC'))
        }), 422

    @staticmethod
    def handle_precondition_failed_exception(e):
        """
        Handles PreconditionFailedException.
        Use this handler when a precondition specified in the request headers is not met.
        """
        return jsonify({
            'message': 'Precondition failed.',
            'error': 'Precondition Failed Exception: ' + str(e),
            'error_code': '4121',
            'timestamp': datetime.now(ZoneInfo('UTC'))
        }), 412

    @staticmethod
    def handle_unsupported_media_type(e):
        """
        Handles Unsupported Media Type errors.
        Use this handler when the request's Content-Type is not supported.
        """
        return jsonify({
            'message': 'Unsupported Media Type',
            'error': 'Unsupported Media Type Exception: ' + str(e),
            'error_code': '4151',
            'timestamp': datetime.now(ZoneInfo('UTC'))
        }), 415

    @staticmethod
    def handle_gateway_timeout_exception(e):
        """
        Handles GatewayTimeoutException.
        Use this handler for cases where a gateway or proxy server did not receive a timely response from an upstream server.
        """
        return jsonify({
            'message': 'Gateway timeout.',
            'error': 'Gateway Timeout Exception: ' + str(e),
            'error_code': '5041',
            'timestamp': datetime.now(ZoneInfo('UTC'))
        }), 504

    @staticmethod
    def register_error_handlers(app):
        """
        Registers error handlers with the Flask app.
        Maps specific exceptions to their respective handlers.
        """
        app.errorhandler(MissingDataException)(ErrorHandlers.handle_missing_data_exception)
        app.errorhandler(MissingCredentialsException)(ErrorHandlers.handle_missing_credentials_exception)
        app.errorhandler(CredentialsUnauthorizedException)(ErrorHandlers.handle_custom_unauthorized_exception)
        app.errorhandler(MethodNotAllowedException)(ErrorHandlers.handle_method_not_allowed_exception)
        app.errorhandler(NotFoundException)(ErrorHandlers.handle_not_found_exception)
        app.errorhandler(ConflictException)(ErrorHandlers.handle_conflict_exception)
        app.errorhandler(UnprocessableEntityException)(ErrorHandlers.handle_unprocessable_entity_exception)
        app.errorhandler(PreconditionFailedException)(ErrorHandlers.handle_precondition_failed_exception)
        app.errorhandler(GatewayTimeoutException)(ErrorHandlers.handle_gateway_timeout_exception)
        app.errorhandler(TokenUnauthorizedException)(ErrorHandlers.handle_unauthorized_token_error)
        app.errorhandler(InternalServerException)(ErrorHandlers.handle_internal_server_error)
        app.errorhandler(BadRequestException)(ErrorHandlers.handle_bad_request_error)
        app.errorhandler(UnsupportedMediaTypeException)(ErrorHandlers.handle_unsupported_media_type)
