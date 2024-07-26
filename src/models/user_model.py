# /src/models/user_model.py

from src.configs.development_config import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128))

    def set_password(self, password):
        self.password = password

    def check_password(self, password):
        return self.password == password



