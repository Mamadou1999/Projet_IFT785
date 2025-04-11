from services.jobposting import Company
from services.jobposting import JobPosting

def test_company_specific_attributes(company_data):
    """
        Vérifie que les attributs spécifiques à l'entreprise sont correctement gérés
    """
    company = Company(**company_data)
    assert company.company_name == "Startup Inc."
    assert company.description == "A small innovative startup."

def test_company_job_postings_relation(company_data):
    """
        Vérifie que l'entreprise peut gérer ses fiches de poste
    """
    company = Company(**company_data)
    job1 = JobPosting(title="Backend Dev", company=company)
    job2 = JobPosting(title="Frontend Dev", company=company)
    company.create_job_offer(job1)
    company.create_job_offer(job2)

    # On doit vérifier que les job1 et job2 sont bien rattachés à la compagnie
