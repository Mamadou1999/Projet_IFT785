from services.jobposting import JobPosting

def test_job_posting_creation():
    """
        Vérifie la création correcte d'une fiche de poste
    """
    job = JobPosting(
        title="Backend Developer",
        location="Remote",
        technologies=["Python", "Flask"],
        experience_required=3,
        salary=50000,
        description="Backend job with REST API work"
    )

    assert job.title == "Backend Developer"
    assert job.location == "Remote"
    assert "Flask" in job.technologies
    assert job.salary == 50000

def test_job_posting_clone():
    """
        Vérifie la fonctionnalité de clonage d'une fiche de poste
    """
    job = JobPosting(
        title="Frontend Dev",
        location="Paris",
        technologies=["React", "CSS"],
        experience_required=2,
        salary=45000,
        description="UI/UX heavy role"
    )
    cloned = job.clone()

    assert cloned is not job
    assert cloned.title == job.title
    assert cloned.technologies == job.technologies
    assert cloned.description == job.description
