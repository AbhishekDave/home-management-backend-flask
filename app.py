# /app.py

from src.apis import register_blueprint
# from src.configs import load_configurations
from src.configs.development_config import app

# app = load_configurations()

# Register error handlers
register_blueprint(app)

if __name__ == '__main__':
    app.run()
