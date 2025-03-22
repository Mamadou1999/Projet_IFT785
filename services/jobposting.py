from datetime import datetime
from typing import List, Optional
from company import Company

class JobPosting:
    def __init__(self):
        self.id: int = 0
        self.title: str = ""
        self.location: str = ""
        self.technologies: List[str] = []
        self.experience_level: int = 0
        self.salary_range: float = 0.0
        self.description: str = ""
        self.created_at: datetime = datetime.now()
        self.updated_at: Optional[datetime] = None
        self.company: Optional[Company] = None
    
    def clone(self) -> 'JobPosting':
        """Crée une copie de l'offre d'emploi"""
        new_posting = JobPosting()
        new_posting.id = self.id
        new_posting.title = self.title
        new_posting.location = self.location
        new_posting.technologies = self.technologies.copy()
        new_posting.experience_level = self.experience_level
        new_posting.salary_range = self.salary_range
        new_posting.description = self.description
        new_posting.created_at = self.created_at
        new_posting.updated_at = self.updated_at
        new_posting.company = self.company
        return new_posting
    
    def is_active(self) -> bool:
        """Vérifie si l'offre d'emploi est active"""
        # Logique pour vérifier si l'offre est active
        return True
    
    def activate(self):
        """Active l'offre d'emploi"""
        print(f"Offre d'emploi '{self.title}' activée")
    
    def deactivate(self):
        """Désactive l'offre d'emploi"""
        print(f"Offre d'emploi '{self.title}' désactivée")