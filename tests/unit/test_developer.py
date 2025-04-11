from services.developer import Developer

def test_developer_specific_attributes(developer_data):
    """
        Vérifie que les attributs spécifiques au développeur sont correctement gérés
    """
    dev = Developer(**developer_data)
    assert dev.programming_languages == ["Python", "JavaScript"]
    assert dev.experience_levels["JavaScript"] == 3

def test_developer_update_skills(developer_data):
    """
        Vérifie que la mise à jour des compétences fonctionne
    """
    dev = Developer(**developer_data)
    dev.update_profile(["Go", "Rust"], {"Go": 2, "Rust": 4})
    assert "Go" in dev.programming_languages
    assert dev.experience_levels["Rust"] == 4