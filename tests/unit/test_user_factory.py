from services.developer import Developer
from services.company import Company

def test_create_developer_user(user_factory, developer_data):
    """
        Vérifier que la factory crée correctement un utilisateur développeur
    """
    dev = user_factory.create_user("developer")
    dev.programming_languages = developer_data['programmingLanguages']
    dev.experience_levels = developer_data['experienceLevels']
    

    assert isinstance(dev, Developer)
    assert dev._programming_languages == ["Python", "JavaScript"]
    assert dev._experience_levels == 5

def test_create_company_user(user_factory, company_data):
    """
        Vérifier que la factory crée correctement un utilisateur entreprise
    """
    company = user_factory.create_user("company")
    company.email = company_data['email']
    company._description = company_data['description']
    company._company_name = company_data['companyName']

    assert isinstance(company, Company)
    assert company._company_name == "Startup Inc."
    assert company._description == "A small innovative startup."


