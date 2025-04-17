from services.jobpostingbuilder import JobPostingBuilder
from services.jobpostingdirector import JobPostingDirector
from services.company import Company
from services.concreteuserfactory import ConcreteUserFactory

def test_create_senior_job_posting(company_data):
    """
        Vérifie que le director crée correctement une fiche de poste senior
    """

    factory = ConcreteUserFactory()
    company = factory.create_user('company')
    
    company.email = company_data['email']
    company._description = company_data['description']
    company.name = company_data['companyName']
    company.email = company_data['email']

    builder = JobPostingBuilder()
    director = JobPostingDirector(builder)
    job = director.construct_senior_dev_posting(company)

    assert job.experience_level >= 5
    assert job.title == "Développeur Senior"
    assert "senior" in job.description.lower()

def test_create_junior_job_posting(company_data):
    """
        Vérifie que le director crée correctement une fiche de poste junior
    """
    factory = ConcreteUserFactory()
    company = factory.create_user('company')
    
    company.email = company_data['email']
    company._description = company_data['description']
    company.name = company_data['companyName']
    company.email = company_data['email']

    builder = JobPostingBuilder()
    director = JobPostingDirector(builder)
    job = director.construct_junior_dev_posting(company)

    assert job.experience_level <= 2
    assert job.title == "Développeur Junior"
    assert "junior" in job.description.lower()

def test_create_intern_job_posting(company_data):
    """
        Vérifie que le director crée correctement une fiche de poste interne
    """
    factory = ConcreteUserFactory()
    company = factory.create_user('company')
    
    company.email = company_data['email']
    company._description = company_data['description']
    company.name = company_data['companyName']
    company.email = company_data['email']

    builder = JobPostingBuilder()
    director = JobPostingDirector(builder)
    job = director.construct_intern_posting(company)

    assert job.title == "Stage en développement"
    assert "stage" in job.description.lower()
    assert job.experience_level == 0
