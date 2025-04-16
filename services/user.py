# Classe de base User
from typing import Dict, Any

class User:
    def __init__(self):
        self.id = None
        self.email = ""
        self.password = ""
        self.name = ""
        self.surname = ""
        self.created_at = None
        self.updated_at = None
    
    def authenticate(self, email, password):
        print(f"Authentification de l'utilisateur {self.name}")
        return True
    
    def update_profile(self, object):
        print(f"Mise à jour du profil de {self.name}")
        self.updated_at = "current_datetime"

    def get_profile(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }