# Classe de base User
from typing import Dict, Any

class User:
    def __init__(self):
        self._id = None
        self._email = ""
        self._password = ""
        self._name = ""
        self._surname = ""
        self._created_at = None
        self._updated_at = None

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def password(self):
        return self._password
        
    @password.setter
    def password(self, value):
        self._password = value
    
    def update_profile(self, data):
        for key, value in data.items():
            # Ne pas traiter les attributs qui n'existent pas
            if hasattr(self, key):
                setattr(self, key, value)

    def get_profile(self) -> Dict[str, Any]:
        return {
            'id': self._id,
            'name': self._name,
            'surname': self._surname,
            'email': self._email,
            'created_at': self._created_at,
            'updated_at': self._updated_at
        }