# Classe concrète VerifiedProfileDecorator

from services.profildecorator import ProfileDecorator
from typing import Dict, Any

class VerifiedProfileDecorator(ProfileDecorator):

    def __init__(self, user):
        super().__init__(user)
    
    def get_profile(self) -> Dict[str, Any]:
        base_profile = self.user.get_profile()
        base_profile.update({
            'verified': True,
            'verification_badge': True
        })

        return base_profile