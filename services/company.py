from services.user import User
from services.jobposting import JobPosting

# Classe Company qui hérite de User
class Company(User):
    def __init__(self):
        super().__init__()
        self._company_name = ""
        self._description = ""
        self._location = ""
        self._logo = ""
    
    def create_job_offer(self, title, location, technologies, experience_level, salary_range, description):

        job = JobPosting()

        job.title = title
        job.location = location
        job.technologies = technologies
        job.experience_level = experience_level
        job.salary_range = salary_range
        job.description = description
        job.company = self

        return job
    
    def view_developer_profiles(self):
        print(f"Visualisation des profils de développeurs par {self.company_name}")
        return ["developer_profile1", "developer_profile2"]