from profilvisibilitystrategy import ProfileVisibilityStrategy

# Classe concrète PrivateProfileStrategy
class PrivateProfileStrategy(ProfileVisibilityStrategy):
    def display_profile(self, developer):
        print(f"Affichage du profil privé de {developer.name}")
        # Affiche uniquement les informations non sensibles
        private_info = {
            "name": developer.name,
            "programming_languages": developer.programming_languages,
            "location": developer.location
        }
        return private_info