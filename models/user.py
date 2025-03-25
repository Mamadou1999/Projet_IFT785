from datetime import datetime
from app import db

class User(db.Model):

    __tablename__ = 'users'

    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    type = db.Column(db.String(50))  # Pour la classe héritée (Company ou Developer)
    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': type
    }

    def authenticate(self, password):
        return self.password == password  # À remplacer par un hash sécurisé

    def update_profile(self, name, surname):
        self.name = name
        self.surname = surname
