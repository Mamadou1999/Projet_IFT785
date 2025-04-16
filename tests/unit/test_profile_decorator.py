from services.premiumprofildecorator import PremiumProfileDecorator
from services.verifiedprofildecorator import VerifiedProfileDecorator
from services.developer import Developer
from datetime import datetime

def test_verified_profile_decorator(developer_data):
    """
        Vérifie que le décorateur de profil vérifié ajoute les fonctionnalités attendues
    """
    dev = Developer(**developer_data)
    now = datetime.now()
    decorated_dev = VerifiedProfileDecorator(dev, verified_at=now)
    profile = decorated_dev.get_profile()

    assert profile["verified"] is True
    assert profile["verified_at"] == now
    assert profile["verification_badge"] is True

def test_premium_profile_decorator(developer_data):
    """
        Vérifie que le décorateur de profil premium ajoute les fonctionnalités attendues
    """
    dev = Developer(**developer_data)
    future_date = datetime.now().replace(year=datetime.now().year + 1)
    decorated_dev = PremiumProfileDecorator(dev, subscription_expiry=future_date)
    profile = decorated_dev.get_profile()

    assert profile["premium"] is True
    assert profile["premium_badge"] is True
    assert profile["premium_features"] == {
        "advanced_search": True,
        "priority_support": True
    }
