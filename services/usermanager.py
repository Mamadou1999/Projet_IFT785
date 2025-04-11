from services.usersubject import UserSubject
from services.concreteuserfactory import ConcreteUserFactory



# Classe UserManager qui implémente UserSubject
class UserManager(UserSubject):
    def __init__(self):
        self.observers = []
    
    def attach(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
    
    def detach(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
    
    def notify(self, event):
        for observer in self.observers:
            observer.update(self.current_user, event)
    
    def register_user(self, type, user_data):
        factory = ConcreteUserFactory()
        user = factory.create_user(type)
        user.email = user_data.get('email')
        user.name = user_data.get('name')
        user.surname = user_data.get('surname')
        user.password = user_data.get('password')
        self.current_user = user
        self.notify("user_registered")
        return user
    
    def update_user_profile(self, userid, user_data):
        # Logique pour mettre à jour le profil utilisateur
        self.current_user.update_profile()
        self.notify("profile_updated")