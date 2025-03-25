from flask import Flask, request, jsonify, Blueprint
from app.models.job import Job
from flask_jwt_extended import  jwt_required
from app import db



job_bp = Blueprint('job', __name__)


# GESTION DES OFFRES D’EMPLOI
@job_bp.route('/jobs', methods=['GET'])
def get_jobs():
    jobs = Job.query.all()
    return jsonify([job.to_dict() for job in jobs])

@job_bp.route('/jobs/create', methods=['POST'])
@jwt_required()
def create_job():
    data = request.json
    job = Job(**data)
    db.session.add(job)
    db.session.commit()
    return jsonify({'message': 'Offre créée avec succès'}), 201