# src/apis/grocery_api/grocery_type_post.py

from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import SQLAlchemyError

from src.configs.development_config import db
from src.decorators.unified_decorators.validate_request import validate_request

from src.models.grocery_models.grocery_name_model import GroceryName
from src.schemas.grocery_schemas.grocery_name_schema import GroceryNameSchema

grocery_name_post_api_bp = Blueprint('grocery_name_api', __name__)