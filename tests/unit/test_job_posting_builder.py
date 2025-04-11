from services.jobpostingbuilder import JobPostingBuilder

def test_job_posting_builder_fluid_interface():
    """
        Vérifie que l'interface fluide du builder fonctionne correctement
    """
    builder = JobPostingBuilder()
    result = builder.with_title("DevOps Engineer").with_location("Lyon")
    assert isinstance(result, JobPostingBuilder)  # permet le chaînage

def test_job_posting_builder_build():
    """
        Vérifie que le builder construit correctement une fiche de poste
    """
    builder = JobPostingBuilder()
    job = (
        builder
        .with_title("Fullstack Developer")
        .with_location("Marseille")
        .with_technologies(["Vue", "Node.js"])
        .with_experience_level(3)
        .with_salary_range(55000)
        .with_description("Fullstack web dev")
        .build()
    )

    assert job.title == "Fullstack Developer"
    assert "Vue" in job.technologies
    assert job.salary_range == 55000
