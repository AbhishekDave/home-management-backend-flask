# src/apis/__init__.py

# API Version
from src.configs.development_config import API_VERSION_1                            # API version 'v1' from .env file

# Auth_APIs
from src.apis.auth_api.register import register_api_bp                              # API endpoint: /v1/auth/register
from src.apis.auth_api.login import login_api_bp                                    # API endpoint: /v1/auth/login
from src.apis.auth_api.logout import logout_api_bp                                  # API endpoint: /v1/auth/logout
from src.apis.auth_api.protected import protected_api_bp                            # API endpoint: /v1/auth/protected
from src.apis.auth_api.refresh import refresh_api_bp                                # API endpoint: /v1/auth/refresh
from src.apis.auth_api.forgot_password import forgot_password_api_bp                # API endpoint: /v1/auth/forgot-password
from src.apis.auth_api.reset_password import reset_password_api_bp                  # API endpoint: /v1/auth/reset-password

# User_APIs
from src.apis.user_api.user_api_get import user_api_get_bp                         # API endpoint: /v1/user/grocery-name-lists

# Grocery_APIs
from src.apis.grocery_api.grocery_api_post import grocery_name_post_api_bp
from src.apis.grocery_api.grocery_api_get import grocery_name_get_api_bp

# Store_APIs
from src.apis.store_api.store_api_post import store_api_post_bp


def register_blueprint(app):
    # Auth APIs
    app.register_blueprint(register_api_bp, url_prefix=f'/{API_VERSION_1}/auth')
    app.register_blueprint(login_api_bp, url_prefix=f'/{API_VERSION_1}/auth')
    app.register_blueprint(refresh_api_bp, url_prefix=f'/{API_VERSION_1}/auth')
    app.register_blueprint(protected_api_bp, url_prefix=f'/{API_VERSION_1}/auth')
    app.register_blueprint(logout_api_bp, url_prefix=f'/{API_VERSION_1}/auth')
    app.register_blueprint(forgot_password_api_bp, url_prefix=f'/{API_VERSION_1}/auth')
    app.register_blueprint(reset_password_api_bp, url_prefix=f'/{API_VERSION_1}/auth')

    # User APIs
    app.register_blueprint(user_api_get_bp, url_prefix=f'/{API_VERSION_1}')
    # Grocery APIs
    app.register_blueprint(grocery_name_post_api_bp, url_prefix=f'/{API_VERSION_1}')
    app.register_blueprint(grocery_name_get_api_bp, url_prefix=f'/{API_VERSION_1}')

    # Store APIs
    app.register_blueprint(store_api_post_bp, url_prefix=f'/{API_VERSION_1}')
