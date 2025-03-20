# Classe de base User
class User:
    def __init__(self):
        self.id = None
        self.email = ""
        self.password = ""
        self.name = ""
        self.surname = ""
        self.created_at = None
        self.updated_at = None
    
    def authenticate(self):
        print(f"Authentification de l'utilisateur {self.name}")
        return True
    
    def update_profile(self):
        print(f"Mise à jour du profil de {self.name}")
        self.updated_at = "current_datetime"