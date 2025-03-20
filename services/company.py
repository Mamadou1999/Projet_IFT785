from user import User

# Classe Company qui hérite de User
class Company(User):
    def __init__(self):
        super().__init__()
        self.company_name = ""
        self.description = ""
        self.location = ""
        self.logo = ""
    
    def create_job_offer(self):
        print(f"Création d'une offre d'emploi par {self.company_name}")
        return "job_offer"
    
    def view_developer_profiles(self):
        print(f"Visualisation des profils de développeurs par {self.company_name}")
        return ["developer_profile1", "developer_profile2"]