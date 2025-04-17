from services.concreteuserfactory import ConcreteUserFactory
from services.jobposting import JobPosting

def test_job_posting_creation(company_data):
    """
        Vérifie la création correcte d'une fiche de poste
    """
    factory = ConcreteUserFactory()
    company = factory.create_user('company')
    
    company.email = company_data['email']
    company._description = company_data['description']
    company.name = company_data['companyName']

    job = company.create_job_offer("Backend Developer", "Remote", ["Python", "Flask"], 5, "50000 - 65000", "Backend job with REST API work")

    assert job.title == "Backend Developer"
    assert job.location == "Remote"
    assert "Flask" in job.technologies
    assert job.salary_range == "50000 - 65000"

def test_job_posting_clone(company_data):
    """
        Vérifie la fonctionnalité de clonage d'une fiche de poste
    """
    factory = ConcreteUserFactory()
    company = factory.create_user('company')
    
    company.email = company_data['email']
    company._description = company_data['description']
    company.name = company_data['companyName']

    job = company.create_job_offer("Backend Developer", "Remote", ["Python", "Flask"], 5, "50000 - 65000", "Backend job with REST API work")

    cloned = job.clone()

    assert cloned is not job
    assert cloned.title == job.title
    assert cloned.technologies == job.technologies
    assert cloned.description == job.description
