# Classe concrète VerifiedProfileDecorator

from services.profildecorator import ProfileDecorator
from typing import Dict, Any
from datetime import datetime

class VerifiedProfileDecorator(ProfileDecorator):

    def __init__(self, user, verified_at):
        super().__init__(user)
        self.verified_at = verified_at or datetime.now()
    
    def get_profile(self) -> Dict[str, Any]:
        base_profile = self.user.get_profile()
        base_profile.update({
            'verified': True,
            'verified_at': self.verified_at,
            'verification_badge': True
        })

        return base_profile