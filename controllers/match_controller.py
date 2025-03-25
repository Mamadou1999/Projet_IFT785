from flask import jsonify, Blueprint


match_bp = Blueprint('match', __name__)


# MATCHING
@match_bp.route('/match/developer/<int:dev_id>', methods=['GET'])
def match_developer(dev_id):
    # Logique de matching...
    return jsonify({'message': 'Matching en cours...'})

@match_bp.route('/match/company/<int:company_id>', methods=['GET'])
def match_company(company_id):
    # Logique de matching...
    return jsonify({'message': 'Matching en cours...'})