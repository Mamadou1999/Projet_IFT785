from flask import jsonify, Blueprint, request
from flask_jwt_extended import jwt_required


rating_bp = Blueprint('rating', __name__)


#ÉVALUATIONS
@rating_bp.route('/rating/developer/<int:dev_id>', methods=['POST'])
@jwt_required()
def rate_developer(dev_id):
    data = request.json
    # Ajouter une note au développeur
    return jsonify({'message': 'Note ajoutée'})
