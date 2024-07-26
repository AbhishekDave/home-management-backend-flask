
# src/

def register_blueprint(app):
    from .auth_api.login import login_api_bp
    app.register_blueprint(login_api_bp, url_prefix='/auth')
