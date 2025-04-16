from flask_jwt_extended import  jwt_required
from flask import request, jsonify, Blueprint, render_template,redirect, url_for, flash
from app.models.user import User
from app import db
from flask_login import current_user
from app.services.edit_profile_form import UpdateProfileForm
from app.models.developer import Developer


profile_bp = Blueprint('profile', __name__)


# GESTION DES PROFILS
@profile_bp.route('/profile/<int:user_id>', methods=['GET'])
def get_profile(user_id):
    
    developer = Developer.query.get(user_id)

    return render_template('developer/profile.html', developer=developer)

@profile_bp.route('/profile/<int:user_id>/update', methods=['GET', 'POST'])  
def update_profile(user_id):
    form = UpdateProfileForm(obj=current_user)

    if form.validate_on_submit():
        # Peupler les autres champs normalement
        form.populate_obj(current_user)

        # Récupérer les données du champ "programming_languages" et les transformer en liste
        raw_languages = form.programming_languages.data
        parsed_languages = [lang.strip() for lang in raw_languages.split(',') if lang.strip()]

        print(parsed_languages)

        #Remplacer temporairement la valeur brute par la version propre
        current_user.programming_languages = parsed_languages

        db.session.commit()
        flash("Profil mis à jour avec succès ✅", "success")
        return redirect(url_for('profile.get_profile', user_id=current_user.id))

    return render_template('developer/edit_profile.html', form=form)