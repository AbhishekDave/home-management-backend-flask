# jwt_error_handlers.py
from flask import Flask, jsonify
from flask_jwt_extended.exceptions import (
    CSRFError,
    JWTDecodeError,
    NoAuthorizationError,
    RevokedTokenError,
    UserClaimsVerificationError,
    UserLookupError,
    WrongTokenError

)


class JWTErrorHandlers:
    @staticmethod
    def handle_csrf_error(e):
        return jsonify({
            'message': 'CSRF validation failed.',
            'error': str(e)
        }), 401

    @staticmethod
    def handle_jwt_decode_error(e):
        return jsonify({
            'message': 'JWT decode error.',
            'error': str(e)
        }), 401

    @staticmethod
    def handle_no_authorization_error(e):
        return jsonify({
            'message': 'No authorization token provided.',
            'error': str(e)
        }), 401

    @staticmethod
    def handle_revoked_token_error(jwt_header, jwt_data):
        return jsonify({
            'message': 'Token has been revoked.',
            'jwt_header': jwt_header,
            'jwt_data': jwt_data
        }), 401

    @staticmethod
    def handle_user_lookup_error(jwt_header, jwt_data):
        return jsonify({
            'message': 'User lookup failed.',
            'jwt_header': jwt_header,
            'jwt_data': jwt_data
        }), 401

    @staticmethod
    def handle_user_claims_verification_error(jwt_header, jwt_data):
        return jsonify({
            'message': 'User claims verification failed.',
            'jwt_header': jwt_header,
            'jwt_data': jwt_data
        }), 401

    @staticmethod
    def handle_wrong_token_error(e):
        return jsonify({
            'message': 'Wrong token error.',
            'error': str(e)
        }), 401

    @classmethod
    def register_error_handlers(cls, app: Flask) -> None:
        @app.errorhandler(CSRFError)
        def handle_csrf_error_wrapper(e):
            return cls.handle_csrf_error(e)

        @app.errorhandler(JWTDecodeError)
        def handle_jwt_decode_error_wrapper(e):
            return cls.handle_jwt_decode_error(e)

        @app.errorhandler(NoAuthorizationError)
        def handle_auth_error_wrapper(e):
            return cls.handle_no_authorization_error(e)

        @app.errorhandler(RevokedTokenError)
        def handle_revoked_token_error_wrapper(e):
            return cls.handle_revoked_token_error(e.jwt_header, e.jwt_data)

        @app.errorhandler(UserLookupError)
        def handle_user_lookup_error_wrapper(e):
            return cls.handle_user_lookup_error(e.jwt_header, e.jwt_data)

        @app.errorhandler(UserClaimsVerificationError)
        def handle_failed_token_verification_wrapper(e):
            return cls.handle_user_claims_verification_error(e.jwt_header, e.jwt_data)

        @app.errorhandler(WrongTokenError)
        def handle_wrong_token_error_wrapper(e):
            return cls.handle_wrong_token_error(e)
