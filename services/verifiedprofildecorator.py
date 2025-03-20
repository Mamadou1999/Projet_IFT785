from profildecorator import ProfileDecorator
# Classe concrète VerifiedProfileDecorator
class VerifiedProfileDecorator(ProfileDecorator):
    def get_profile(self):
        base_profile = self.user.__dict__.copy()
        base_profile["verified"] = True
        return base_profile