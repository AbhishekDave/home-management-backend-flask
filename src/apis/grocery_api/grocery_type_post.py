# src/apis/grocery_api/grocery_type_post.py

from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import SQLAlchemyError

from src.configs.development_config import db
from src.decorators.unified_decorators.validate_request import validate_request

from src.models.grocery_models.grocery_name_model import GroceryName
from src.schemas.grocery_schemas.grocery_name_schema import GroceryNameSchema

grocery_name_post_api_bp = Blueprint('grocery_name_api', __name__)


@grocery_name_post_api_bp.route('/grocery-names', methods=['POST'])
@jwt_required()
@validate_request('POST', schema=GroceryNameSchema())
def add_grocery_type(**kwargs):
    # Log the incoming request URL
    api_url = request.url
    current_app.logger.info(f"\nRequest URL: {api_url}")

    current_user = get_jwt_identity()
    name = kwargs.get('validated_data', {}).get('name')    # Access validated data

    try:
        # Check if grocery type already exists
        grocery_type = GroceryName.query.filter_by(name=name).first()

        if grocery_type is None:
            # Create a new grocery type if it does not exist
            new_grocery_type = GroceryName(name=name)
            db.session.add(new_grocery_type)
            db.session.commit()
            grocery_type_id = new_grocery_type.id
            grocery_type_data = GroceryNameSchema().dump(new_grocery_type)
            message = 'Grocery Type Added Successfully'
        else:
            # Use existing grocery type ID
            grocery_type_data = GroceryNameSchema().dump(grocery_type)
            message = 'User is already linked to this grocery type'

        current_app.logger.info(f"\nGrocery type added: \nName - {name} \nby user: {current_user}")
        return jsonify({
            "user_id": current_user,
            "grocery_type_data": grocery_type_data,
            "message": message
        }), 201

    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback the session in case of an error
        current_app.logger.error(f"\nDatabase error occurred: {e}")
        return jsonify({"msg": "Database error occurred", "error": str(e)}), 500

    except Exception as e:
        # Log the exception for debugging
        current_app.logger.error(f"\nAn unexpected error occurred: {e}")
        return jsonify({"msg": "An unexpected error occurred", "error": str(e)}), 500
