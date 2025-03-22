from jobposting import JobPosting
from company import Company
from typing import List, Optional


class JobPostingBuilder:
    def __init__(self):
        self.job_posting: JobPosting = JobPosting()
    
    def with_title(self, title: str) -> 'JobPostingBuilder':
        """Définit le titre de l'offre d'emploi"""
        self.job_posting.title = title
        return self
    
    def with_location(self, location: str) -> 'JobPostingBuilder':
        """Définit le lieu de l'offre d'emploi"""
        self.job_posting.location = location
        return self
    
    def with_technologies(self, technologies: List[str]) -> 'JobPostingBuilder':
        """Définit les technologies requises pour l'offre d'emploi"""
        self.job_posting.technologies = technologies
        return self
    
    def with_experience_level(self, level: int) -> 'JobPostingBuilder':
        """Définit le niveau d'expérience requis pour l'offre d'emploi"""
        self.job_posting.experience_level = level
        return self
    
    def with_salary_range(self, range: float) -> 'JobPostingBuilder':
        """Définit la fourchette de salaire pour l'offre d'emploi"""
        self.job_posting.salary_range = range
        return self
    
    def with_description(self, description: str) -> 'JobPostingBuilder':
        """Définit la description de l'offre d'emploi"""
        self.job_posting.description = description
        return self
    
    def with_company(self, company: Company) -> 'JobPostingBuilder':
        """Définit l'entreprise associée à l'offre d'emploi"""
        self.job_posting.company = company
        return self
    
    def build(self) -> JobPosting:
        """Construit et retourne l'offre d'emploi"""
        return self.job_posting