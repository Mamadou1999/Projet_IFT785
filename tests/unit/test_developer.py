from services.developer import Developer
from services.concreteuserfactory import ConcreteUserFactory

def test_developer_specific_attributes(developer_data):
    """
        Vérifie que les attributs spécifiques au développeur sont correctement gérés
    """
    factory =  ConcreteUserFactory()
    dev = factory.create_user('Developer')
    dev.programming_languages = developer_data['programmingLanguages']
    dev.experience_levels = developer_data['experienceLevels']

    assert dev.programming_languages == ["Python", "JavaScript"]
    assert dev.experience_levels == 5

def test_developer_update_skills(developer_data):
    """
        Vérifie que la mise à jour des compétences fonctionne
    """
    factory =  ConcreteUserFactory()
    dev = factory.create_user('Developer')
    dev.programming_languages = developer_data['programmingLanguages']
    dev.experience_levels = developer_data['experienceLevels']

    dev.update_profile(
        {
            "programming_languages": ["Python", "JavaScript", "Java"],
            "experience_levels": 6
        }
    )
    assert "Java" in dev.programming_languages
    assert dev.experience_levels == 6