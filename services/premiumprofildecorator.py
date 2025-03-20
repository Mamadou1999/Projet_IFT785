from profildecorator import ProfileDecorator
# Classe concrète PremiumProfileDecorator
class PremiumProfileDecorator(ProfileDecorator):
    def get_profile(self):
        base_profile = self.user.__dict__.copy()
        base_profile["premium"] = True
        base_profile["featured"] = True
        return base_profile