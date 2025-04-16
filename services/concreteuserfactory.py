from services.userfactory import UserFactory
from services.user import User
from services.developer import Developer
from services.company import Company

# Classe concrète ConcreteUserFactory
class ConcreteUserFactory(UserFactory):
    def create_user(self, type):
        if type == "developer":
            return Developer()
        elif type == "company":
            return Company()
        else:
            return User()