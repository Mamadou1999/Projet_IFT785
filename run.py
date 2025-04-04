from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Données fictifs pour les tests
    popular_devs = [
        {'id': 1, 'name': "Alice Dupont", "bio": "Développeuse Full Stack passionnée.", "profile_image_url": None},
        {'id': 2, 'name': "Bob Martin", "bio": "Expert en IA et Machine Learning.", "profile_image_url": None},
        {'id': 3, 'name': 'Charlie Nguyen', 'bio': "Développeur mobile avec 5 ans d'expérience.", "profile_image_url": None}
    ]

    recent_jobs = [
        {'id': 101, 'title': 'Développeur Backend Python', 'company_name': 'Tech Corp', 'location': 'Paris', 'description': 'Rejoignez notre équipe dynamique.'},
        {'id': 102, 'title': 'Frontend React Developer', 'company_name': 'Web Solutions', 'location': 'Lyon', 'description': 'Cherchons passionné(e) du front-end.'},
        {'id': 103, 'title': 'Data Scientist', 'company_name': 'DataWorld', 'location': 'Remote', 'description': 'Analysez et donnez du sens aux données.'}
    ]

    return render_template('index.html', popular_devs=popular_devs, recent_jobs=recent_jobs)

if __name__ == '__main__':
    app.run(debug=True)
