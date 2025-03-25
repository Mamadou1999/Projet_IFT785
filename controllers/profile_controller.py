from flask_jwt_extended import  jwt_required
from flask import request, jsonify, Blueprint
from app.models.user import User
from app import db


profile_bp = Blueprint('profile', __name__)


# GESTION DES PROFILS
@profile_bp.route('/profile/<int:user_id>', methods=['GET'])
def get_profile(user_id):
    user = User.query.get(user_id)
    return jsonify(user.to_dict()) if user else jsonify({'message': 'Utilisateur non trouvé'}), 404

@profile_bp.route('/profile/<int:user_id>/update', methods=['PUT'])
@jwt_required()
def update_profile(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'Utilisateur non trouvé'}), 404
    data = request.json
    for key, value in data.items():
        setattr(user, key, value)
    db.session.commit()
    return jsonify({'message': 'Profil mis à jour'})