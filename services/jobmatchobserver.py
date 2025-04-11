from services.userobserver import UserObserver
# Classe concrète JobMatchObserver
class JobMatchObserver(UserObserver):

    def update(self, user, event):
        print(f"JobMatchObserver: Mise à jour pour l'utilisateur {user.name} avec l'événement '{event}'")