# routes/job_controller.py (ou ce que tu utilises)

from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_required
from app.services.job_form import JobForm
from app.models.job import Job
from app.extensions import db

job_bp = Blueprint('job', __name__)

@job_bp.route('/job/<int:job_id>', methods=['GET'])
def get_job(job_id):
    
    job = Job.query.get(job_id)

    return render_template('company/job_details.html', job=job)

@job_bp.route('/job/create', methods=['GET', 'POST'])
@login_required
def create_job():
    form = JobForm()

    if form.validate_on_submit():
        job = Job(
            title=form.title.data,
            company_name=form.company_name.data,
            location=form.location.data,
            description=form.description.data,
            requirements=form.requirements.data,
            company_id=current_user.id,
            salary_range=form.salary_range.data

        )
        db.session.add(job)
        db.session.commit()
        flash("Offre d'emploi publiée avec succès ✅", "success")
        return redirect(url_for('auth.dashboard'))
    
    return render_template('company/create_job.html', form=form)

@job_bp.route('job/<int:job_id>/edit', methods=['GET', 'POST'])  # Utilisez POST au lieu de PUT
def edit_job(job_id):
    job = Job.query.get_or_404(job_id)

    # Vérifie que l'utilisateur connecté est bien le propriétaire du job
    if job.company_id != current_user.id:
        flash("Vous n'êtes pas autorisé à modifier cette offre.", "danger")
        return redirect(url_for('auth.dashboard'))

    form = JobForm(obj=job)

    if form.validate_on_submit():
        # Mettre à jour les champs du job
        job.title = form.title.data
        job.location = form.location.data
        job.description = form.description.data
        job.requirements = form.requirements.data
        job.salary_range = form.salary_range.data

        db.session.commit()
        flash("Offre d'emploi mise à jour avec succès ✅", "success")
        return redirect(url_for('auth.company_dashboard'))

    return render_template('company/edit_job.html', form=form, job=job)