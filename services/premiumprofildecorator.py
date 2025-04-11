# Classe concrète PremiumProfileDecorator

from services.profildecorator import ProfileDecorator
from typing import Dict, Any
from datetime import datetime

class PremiumProfileDecorator(ProfileDecorator):

    def __init__(self, user, subscription_expiry):
        super().__init__(user)
        self.subscription_expiry = subscription_expiry or datetime.now().replace(year=datetime.now().year + 1)
    
    def get_profile(self) -> Dict[str, Any]:
        base_profile = self.user.get_profile()
        base_profile.update({
            'premium': True,
            'premium_badge': True,
            'premium_features': self._get_premium_features()
        })
        
        return base_profile
    
    def _get_premium_features(self):
        features = {
            'advanced_search': True,
            'priority_support': True
        }

        return features