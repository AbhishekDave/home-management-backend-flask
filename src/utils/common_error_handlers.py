# src/utils/common_error_handlers.py

from flask import jsonify


class ErrorHandlers:
    @staticmethod
    def handle_401_error(e):
        return jsonify({
            'message': 'Unauthorized: Token expired or invalid.',
            'error': str(e)
        }), 401

    @staticmethod
    def handle_500_error(e):
        return jsonify({
            'message': 'Internal Server Error',
            'error': str(e)
        }), 500

    @staticmethod
    def register_error_handlers(app):
        app.errorhandler(401)(ErrorHandlers.handle_401_error)
        app.errorhandler(500)(ErrorHandlers.handle_500_error)
