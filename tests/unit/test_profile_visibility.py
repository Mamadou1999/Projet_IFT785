from services.privateprofilstrategy import PrivateProfileStrategy
from services.publicprofilstrategy import PublicProfileStrategy

from services.developer import Developer

def test_public_profile_strategy(developer_data):
    """
        Vérifie le comportement de la stratégie de profil public
    """
    dev = Developer(**developer_data)
    dev.set_profile_strategy(PublicProfileStrategy())
    profile_view = dev.get_profile_view()
    
    assert "email" in profile_view
    assert "salary" in profile_view
    assert profile_view["email"] == "dev@example.com"

def test_private_profile_strategy(developer_data):
    """
        Vérifie le comportement de la stratégie de profil privé
    """
    dev = Developer(**developer_data)
    dev.salary = 40000
    dev.set_profile_strategy(PrivateProfileStrategy())
    profile_view = dev.get_profile_view()
    
    assert "email" not in profile_view
    assert "salary" not in profile_view
