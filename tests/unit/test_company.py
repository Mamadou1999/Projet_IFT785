from services.jobposting import JobPosting
from services.concreteuserfactory import ConcreteUserFactory

def test_company_specific_attributes(company_data):
    """
        Vérifie que les attributs spécifiques à l'entreprise sont correctement gérés
    """
    
    factory = ConcreteUserFactory()
    company = factory.create_user('company')
    
    company.email = company_data['email']
    company._description = company_data['description']
    company.name = company_data['companyName']

    assert company.name == "Startup Inc."
    assert company.email == "contact@startup.com" 
    assert company._description == "A small innovative startup."

def test_company_job_postings_relation(company_data):
    """
        Vérifie que l'entreprise peut gérer ses fiches de poste
    """
    factory = ConcreteUserFactory()
    company = factory.create_user('company')
    
    company.email = company_data['email']
    company._description = company_data['description']
    company.name = company_data['companyName']

    job1 = JobPosting()
    job1.title = "Backend Dev"
    job1.company = company

    job2 = JobPosting()
    job2.title = "Frontend Dev"
    job2.company = company

    assert job1.company.name == "Startup Inc."
    assert job2.company.name == "Startup Inc."
