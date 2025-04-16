from flask import Flask, request, jsonify, Blueprint, render_template, redirect, url_for, flash, session
from flask_jwt_extended import create_access_token, jwt_required
from app.models.user import User
from app.models.company import Company
from app.models.developer import Developer
from app.extensions import db
from app.services.forms import RegisterForm
from app.services.login_form import LoginForm
from app.services.company_form import CompanyForm
from werkzeug.security import generate_password_hash
from flask_login import login_user, login_required, current_user, logout_user
from app.models.job import Job
import re


# Blueprint pour la gestion des utilisateurs
auth_bp = Blueprint('auth', __name__)



def parse_salary_range(salary_range_str):
    """
    Extrait proprement la fourchette salariale (min, max) depuis une string.
    Fonctionne avec des formats comme :
    - '75000$–100000$ /an'
    - '80k - 100k'
    - '70 000 – 90 000'
    - '60000'
    """
    if not salary_range_str:
        return None, None

    # Remplacer les k par "000"
    salary_range_str = salary_range_str.lower().replace('k', '000')

    # Enlever les espaces, $, €, CAD, /an, etc.
    cleaned = re.sub(r'[^0-9\-–]', '', salary_range_str)

    # Séparer min et max par tiret (– ou -)
    parts = re.split(r'[-–]', cleaned)

    if len(parts) == 2:
        try:
            return int(parts[0]), int(parts[1])
        except ValueError:
            return None, None
    elif len(parts) == 1:
        try:
            val = int(parts[0])
            return val, val
        except ValueError:
            return None, None
    else:
        return None, None




def get_matching_jobs_for_developer(developer):
    matching_jobs = []

    all_jobs = Job.query.all()

    for job in all_jobs:
        # Vérification langage
        job_langs = extract_required_languages(job.requirements)
        dev_skills = [s.lower() for s in developer.programming_languages or []]
        
        #Calcul du nombre de correspondances
        match_count = sum(1 for lang in job_langs if lang.lower() in dev_skills)

        # Définir un seuil (ex: 60% ou 3 minimum)
        min_required = min(3, len(job_langs))  

        skill_match = match_count >= min_required

        # Localisation match simple
        location_match = (developer.location.lower() in job.location.lower()) or ("télétravail" in job.location.lower())

        # Salaire
        job_salary_min, job_salary_max = parse_salary_range(job.salary_range)
        dev_min_salary = developer.minimum_salary or 0

        salary_match = (
            job_salary_min is not None and
            job_salary_max is not None and
            job_salary_min <= dev_min_salary <= job_salary_max
        )


        if skill_match and location_match and salary_match:
            matching_jobs.append(job)

    return matching_jobs


def extract_required_languages(requirements_text):
    if not requirements_text:
        return []

    keywords = ['python', 'javascript', 'flask', 'django', 'html/css', 'sql', 'react', 'vue', 'docker', 'pandas', 'notebooks jupyter', 'numpy', 'scikit-learn', 'nodejs', 'flutter']
    found = []

    for word in keywords:
        if word.lower() in requirements_text.lower():
            found.append(word)

    return found


# AUTHENTIFICATION
@auth_bp.route('/register/developer', methods=['GET', 'POST'])
def register_developer():
    form = RegisterForm()

    if form.validate_on_submit():
        data = request.form.to_dict()
        if 'csrf_token' in data:
            data.pop('csrf_token')

        # S'assurer que surname a une valeur
        if 'surname' not in data or not data['surname']:
            data['surname'] = data.get('name', '').split()[0]  # Utilise le premier mot du nom comme surname par défaut

         # Hacher le mot de passe avant de créer l'utilisateur
        plain_password = data.pop('password')  # Retirer le mot de passe en clair
        data['password'] = generate_password_hash(plain_password)  # Ajouter le mot de passe haché

        dev = Developer(**data)
        db.session.add(dev)
        db.session.commit()
        
        return redirect(url_for('auth.login'))  # redirection après succès

    
    return render_template('authentication/register_dev.html', form=form)


@auth_bp.route('/register/company', methods=['GET', 'POST'])
def register_company():
    form = CompanyForm()

    if form.validate_on_submit():
        data = request.form.to_dict()
        if 'csrf_token' in data:
            data.pop('csrf_token')

        if 'name' not in data or not data['name']:
            data['name'] = data.get('company_name', 'Contact')

        data['surname'] = data.get('name', '')

        
         # Hacher le mot de passe avant de créer l'utilisateur
        plain_password = data.pop('password')  # Retirer le mot de passe en clair
        data['password'] = generate_password_hash(plain_password)  # Ajouter le mot de passe haché

        company = Company(**data)
        db.session.add(company)
        db.session.commit()
        
        return redirect(url_for('auth.login'))  # redirection après succès

    
    return render_template('authentication/register_company.html', form=form)

@auth_bp.route('/dashboard')
def dashboard():
    # user_id = session.get('user_id')
    # user = User.query.get(user_id)
    recommended_jobs = get_matching_jobs_for_developer(current_user)
    return render_template('developer/dashboard.html', current_user=current_user, recommended_jobs=recommended_jobs)

@auth_bp.route('/company_dashboard')
def company_dashboard():

    company_jobs= current_user.jobs 
    return render_template('company/dashboard.html', current_user=current_user, company_jobs=company_jobs)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            #access_token = create_access_token(identity=user.name)
            login_user(user)  # ajoute l'utilisateur à la session Flask-Login
            #session['user_id'] = user.id
            flash("Connexion réussie ✅", "success")
            if user.type == 'developer':
                return redirect(url_for('auth.dashboard'))  # dashboard du développeur
            else:
                return redirect(url_for('auth.company_dashboard'))  # dashboard de l'entreprise
        else:
            flash("Identifiants incorrects ❌", "danger")
    return render_template('authentication/login.html', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Déconnecté avec succès 👋", "info")
    return redirect(url_for('index'))


@auth_bp.route('/choose_profile')
def choose_profile():
    # user_id = session.get('user_id')
    # user = User.query.get(user_id)
    return render_template('authentication/choose_profil.html')