from profilvisibilitystrategy import ProfileVisibilityStrategy


# Classe concrète PublicProfileStrategy
class PublicProfileStrategy(ProfileVisibilityStrategy):
    def display_profile(self, developer):
        print(f"Affichage du profil public de {developer.name}")
        # Affiche toutes les informations du développeur
        return developer.__dict__
