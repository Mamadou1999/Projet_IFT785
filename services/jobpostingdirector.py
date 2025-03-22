from jobpostingbuilder import JobPostingBuilder
from company import Company
from jobposting import JobPosting

class JobPostingDirector:
    def __init__(self, builder: JobPostingBuilder):
        self.builder = builder
    
    def construct_senior_dev_posting(self, company: Company) -> JobPosting:
        """Construit une offre d'emploi pour un développeur senior"""
        return (self.builder
                .with_title("Développeur Senior")
                .with_experience_level(5)
                .with_technologies(["Python", "JavaScript", "DevOps"])
                .with_salary_range(70000.0)
                .with_company(company)
                .with_description("Poste de développeur senior avec 5+ ans d'expérience")
                .build())
    
    def construct_junior_dev_posting(self, company: Company) -> JobPosting:
        """Construit une offre d'emploi pour un développeur junior"""
        return (self.builder
                .with_title("Développeur Junior")
                .with_experience_level(1)
                .with_technologies(["HTML", "CSS", "JavaScript"])
                .with_salary_range(45000.0)
                .with_company(company)
                .with_description("Poste de développeur junior, idéal pour les nouveaux diplômés")
                .build())
    
    def construct_intern_posting(self, company: Company) -> JobPosting:
        """Construit une offre d'emploi pour un stagiaire"""
        return (self.builder
                .with_title("Stage en développement")
                .with_experience_level(0)
                .with_technologies(["HTML", "CSS"])
                .with_salary_range(30000.0)
                .with_company(company)
                .with_description("Stage en développement web pour étudiants")
                .build())