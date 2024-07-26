# /app.py

from src.apis import register_blueprint
from src.configs.development_config import app

register_blueprint(app)

if __name__ == '__main__':
    app.run()
