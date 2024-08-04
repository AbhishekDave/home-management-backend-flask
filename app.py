# /app.py

from src.apis import register_blueprint
from src.configs.development_config import create_app

app = create_app()

# Register error handlers
register_blueprint(app)

if __name__ == '__main__':
    app.run()
