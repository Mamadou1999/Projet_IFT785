from services.user import User
from services.publicprofilstrategy import PublicProfileStrategy
from services.privateprofilstrategy import PrivateProfileStrategy


# Classe Developer qui hérite de User
class Developer(User):
    def __init__(self):
        super().__init__()
        self._programming_languages = []
        self._experience_levels = []
        self._minimum_salary = 0
        self._biography = ""
        self._avatar = ""
        self._location = ""
        self._profile_strategy = None

    @property
    def programming_languages(self):
        return self._programming_languages
        
    @programming_languages.setter
    def programming_languages(self, value):
        self._programming_languages = value

    @property
    def experience_levels(self):
        return self._experience_levels
        
    @experience_levels.setter
    def experience_levels(self, value):
        self._experience_levels = value

    @property
    def minimum_salary(self):
        return self._minimum_salary
        
    @minimum_salary.setter
    def minimum_salary(self, value):
        self._minimum_salary = value

    @property
    def biography(self):
        return self._biography
        
    @biography.setter
    def biography(self, value):
        self._biography = value

    @property
    def location(self):
        return self._location
        
    @location.setter
    def location(self, value):
        self._location = value
    
    def show_profile(self):
        print(f"Affichage du profil développeur de {self.name}")
        strategy = self.profile_strategy
        
        return strategy.display_profile(self)

    def set_profile_strategy(self, strategy):
        self.profile_strategy = strategy
