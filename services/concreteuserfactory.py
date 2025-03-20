from userfactory import UserFactory
from user import User
from developer import Developer
from company import Company

# Classe concrète ConcreteUserFactory
class ConcreteUserFactory(UserFactory):
    def create_user(self, type):
        if type == "developer":
            return Developer()
        elif type == "company":
            return Company()
        else:
            return User()