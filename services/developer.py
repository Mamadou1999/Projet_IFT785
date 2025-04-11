from services.user import User
from services.publicprofilstrategy import PublicProfileStrategy
from services.privateprofilstrategy import PrivateProfileStrategy


# Classe Developer qui hérite de User
class Developer(User):
    def __init__(self):
        super().__init__()
        self.programming_languages = []
        self.experience_levels = []
        self.minimum_salary = 0
        self.biography = ""
        self.avatar = ""
        self.location = ""
        self.profile_strategy = None
    
    def show_profile(self):
        print(f"Affichage du profil développeur de {self.name}")
        strategy = PublicProfileStrategy() if self.is_profile_public else PrivateProfileStrategy()
        strategy.display_profile(self)

    def set_profile_strategy(self, strategy):
        self.profile_strategy = strategy
