#

from flask import request, jsonify, Blueprint, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import SQLAlchemyError

from src.configs.development_config import db
from src.models.grocery_models.store_model import Store

from src.schemas.grocery_schemas.store_schema import StoreSchema

from src.decorators.unified_decorators.validate_request import validate_request

store_api_post_bp = Blueprint('store_api_post', __name__)


@store_api_post_bp.route('/stores', methods=['POST'])
@jwt_required()
@validate_request('POST', schema_class=StoreSchema)
def create_store():
    # Log the incoming request URL
    api_url = request.url
    current_app.logger.info(f"\nRequest URL: {api_url}")

    current_user = get_jwt_identity()

    data = request.get_json()

    name = data.get("name")
    description = data.get("description")
    location = data.get("location")

    try:
        store = Store.query.filter_by(name=name).first()

        if store is None:
            new_store = Store(name=name, description=description, location=location)
            db.session.add(new_store)
            db.session.commit()
            store_data = StoreSchema().dump(new_store)
            message = "Store created"
        else:
            store_data = StoreSchema().dump(store)
            message = "Store already exists"

        current_app.logger.info(f"\nStore added: \nName - {name} \nby user: {current_user}")
        return jsonify({
            "message": message,
            "store_data": store_data
        }), 201

    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback the session in case of an error
        current_app.logger.error(f"\nDatabase error occurred: {e}")
        return jsonify({"msg": "Database error occurred", "error": str(e)}), 500

    except Exception as e:
        # Log the exception for debugging
        current_app.logger.error(f"\nAn unexpected error occurred: {e}")
        return jsonify({"msg": "An unexpected error occurred", "error": str(e)}), 500
