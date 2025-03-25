from flask import Flask, request, jsonify, Blueprint
from flask_jwt_extended import create_access_token, jwt_required
from app.models.user import User
from app.models.company import Company
from app.models.developer import Developer
from app import db

# Blueprint pour la gestion des utilisateurs
auth_bp = Blueprint('auth', __name__)

# AUTHENTIFICATION
@auth_bp.route('/register/developer', methods=['POST'])
def register_developer():
    data = request.json
    dev = Developer(**data)
    db.session.add(dev)
    db.session.commit()
    return jsonify({'message': 'Développeur enregistré avec succès !'}), 201

@auth_bp.route('/register/company', methods=['POST'])
def register_company():
    data = request.json
    company = Company(**data)
    db.session.add(company)
    db.session.commit()
    return jsonify({'message': 'Entreprise enregistrée avec succès !'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    return jsonify({'message': 'Identifiants incorrects'}), 401

@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    return jsonify({'message': 'Déconnexion réussie'}), 200