from services.jobpostingbuilder import JobPostingBuilder
from services.jobpostingdirector import JobPostingDirector

def test_create_senior_job_posting():
    """
        Vérifie que le director crée correctement une fiche de poste senior
    """
    builder = JobPostingBuilder()
    director = JobPostingDirector(builder)
    job = director.construct_senior_dev_posting()

    assert job.experience_required >= 5
    assert job.salary >= 60000
    assert "senior" in job.description.lower()

def test_create_junior_job_posting():
    """
        Vérifie que le director crée correctement une fiche de poste junior
    """
    builder = JobPostingBuilder()
    director = JobPostingDirector(builder)
    job = director.construct_junior_dev_posting()

    assert job.experience_required <= 2
    assert job.salary <= 40000
    assert "junior" in job.description.lower()

def test_create_intern_job_posting():
    """
        Vérifie que le director crée correctement une fiche de poste interne
    """
    builder = JobPostingBuilder()
    director = JobPostingDirector(builder)
    job = director.construct_intern_posting()

    assert "intern" in job.description.lower()
