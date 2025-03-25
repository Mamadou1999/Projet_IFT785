from flask import jsonify, Blueprint



search_bp = Blueprint('search', __name__)

# RECHERCHE
@search_bp.route('/search/developers', methods=['GET'])
def search_developers():
    # Logique de recherche...
    return jsonify({'message': 'Résultats de la recherche'})

@search_bp.route('/search/jobs', methods=['GET'])
def search_jobs():
    # Logique de recherche...
    return jsonify({'message': 'Résultats de la recherche'})