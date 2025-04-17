from services.privateprofilstrategy import PrivateProfileStrategy
from services.publicprofilstrategy import PublicProfileStrategy
from services.concreteuserfactory import ConcreteUserFactory

from services.developer import Developer

def test_public_profile_strategy(developer_data):
    """
        Vérifie le comportement de la stratégie de profil public
    """
    factory =  ConcreteUserFactory()
    dev = factory.create_user('developer')
    dev.email = developer_data['email']
    dev.programming_languages = developer_data['programmingLanguages']
    dev.experience_levels = developer_data['experienceLevels']

    dev.set_profile_strategy(PublicProfileStrategy())
    profile_view = dev.show_profile()
    
    assert "_email" in profile_view
    assert "_minimum_salary" in profile_view
    assert profile_view["_email"] == "dev@example.com"

def test_private_profile_strategy(developer_data):
    """
        Vérifie le comportement de la stratégie de profil privé
    """
    factory =  ConcreteUserFactory()
    dev = factory.create_user('developer')
    dev.programming_languages = developer_data['programmingLanguages']
    dev.experience_levels = developer_data['experienceLevels']

    dev.set_profile_strategy(PrivateProfileStrategy())
    profile_view = dev.show_profile()
    
    assert "_email" not in profile_view
    assert "_minimum_salary" not in profile_view
