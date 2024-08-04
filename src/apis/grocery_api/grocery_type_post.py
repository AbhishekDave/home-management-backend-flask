from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from src.configs.development_config import db
from src.models.grocery_models.grocery_type_model import GroceryType
from src.schemas.grocery_schemas.grocery_type_schema import GroceryTypeSchema

grocery_type_post_api_bp = Blueprint('grocery_type_api', __name__)


@grocery_type_post_api_bp.route('/grocery_types', methods=['POST'])
@jwt_required
def create_grocery_type():
    data = request.get_json()

    grocery_type_schema = GroceryTypeSchema()

    new_grocery_type = grocery_type_schema.load(data)
    db.session.add(new_grocery_type)
    db.session.commit()

    grocery_type_data = grocery_type_schema.dump(new_grocery_type)

    return jsonify(grocery_type_data), 201


