from services.userobserver import UserObserver
# Classe concrète ProfileViewObserver
class ProfileViewObserver(UserObserver):
    def update(self, user, event):
        print(f"ProfileViewObserver: Mise à jour pour l'utilisateur {user.name} avec l'événement '{event}'")