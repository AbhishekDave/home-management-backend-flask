# src/apis/__init__.py

from src.apis.auth_api.login import login_api_bp
from src.apis.auth_api.logout import logout_api_bp
from src.apis.auth_api.protected import protected_api_bp
from src.apis.auth_api.refresh import refresh_api_bp
from src.apis.auth_api.register import register_api_bp
from src.configs.development_config import API_VERSION_1


def register_blueprint(app):

    app.register_blueprint(register_api_bp, url_prefix=f'/{API_VERSION_1}/auth')
    app.register_blueprint(login_api_bp, url_prefix=f'/{API_VERSION_1}/auth')
    app.register_blueprint(refresh_api_bp, url_prefix=f'/{API_VERSION_1}/auth')
    app.register_blueprint(protected_api_bp, url_prefix=f'/{API_VERSION_1}/auth')
    app.register_blueprint(logout_api_bp, url_prefix=f'/{API_VERSION_1}/auth')
