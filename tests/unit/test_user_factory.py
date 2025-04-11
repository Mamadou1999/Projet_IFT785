from services.developer import Developer
from services.company import Company

def test_create_developer_user(user_factory, developer_data):
    """
        Vérifier que la factory crée correctement un utilisateur développeur
    """
    dev = user_factory.create_user("developer", **developer_data)

    assert isinstance(dev, Developer)
    assert dev.programming_languages == ["Python", "JavaScript"]
    assert dev.experience_levels["Python"] == 4

def test_create_company_user(user_factory, company_data):
    """
        Vérifier que la factory crée correctement un utilisateur entreprise
    """
    company = user_factory.create_user("company", **company_data)

    assert isinstance(company, Company)
    assert company.company_name == "Startup Inc."
    assert company.description == "A small innovative startup."


