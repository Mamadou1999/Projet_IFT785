from flask import Flask, render_template
import sys
import os


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from app.models.developer import Developer
from app.models.job import Job

app = create_app()

@app.route('/')
def index():
    # Développeurs
    developers = Developer.query.all()  # → liste d’objets User
    # popular_devs = [
    #     {'id': 1, 'name': "Alice Dupont", "bio": "Développeuse Full Stack passionnée.", "profile_image_url": None},
    #     {'id': 2, 'name': "Bob Martin", "bio": "Expert en IA et Machine Learning.", "profile_image_url": None},
    #     {'id': 3, 'name': 'Charlie Nguyen', 'bio': "Développeur mobile avec 5 ans d'expérience.", "profile_image_url": None}
    # ]

    #Jobs
    recent_jobs = Job.query.all()

    # recent_jobs = [
    #     {'id': 101, 'title': 'Développeur Backend Python', 'company_name': 'Tech Corp', 'location': 'Paris', 'description': 'Rejoignez notre équipe dynamique.'},
    #     {'id': 102, 'title': 'Frontend React Developer', 'company_name': 'Web Solutions', 'location': 'Lyon', 'description': 'Cherchons passionné(e) du front-end.'},
    #     {'id': 103, 'title': 'Data Scientist', 'company_name': 'DataWorld', 'location': 'Remote', 'description': 'Analysez et donnez du sens aux données.'}
    # ]

    return render_template('index.html', popular_devs=developers, recent_jobs=recent_jobs)

if __name__ == '__main__':
    app.run(debug=True)
