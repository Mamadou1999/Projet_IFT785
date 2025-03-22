from jobposting import JobPosting
from jobpostingbuilder import JobPostingBuilder
from typing import List, Optional
from datetime import datetime


class JobPostingManager:
    def __init__(self):
        self.active_postings: List[JobPosting] = []
    
    def create_job_posting(self, builder: JobPostingBuilder) -> JobPosting:
        """Crée une nouvelle offre d'emploi à partir du builder"""
        job_posting = builder.build()
        job_posting.id = len(self.active_postings) + 1
        job_posting.created_at = datetime.now()
        self.active_postings.append(job_posting)
        return job_posting
    
    def duplicate_job_posting(self, posting_id: int) -> Optional[JobPosting]:
        """Duplique une offre d'emploi existante"""
        original = self.get_job_posting(posting_id)
        if original:
            duplicate = original.clone()
            duplicate.id = len(self.active_postings) + 1
            duplicate.created_at = datetime.now()
            self.active_postings.append(duplicate)
            return duplicate
        return None
    
    def update_job_posting(self, posting_id: int, builder: JobPostingBuilder) -> Optional[JobPosting]:
        """Met à jour une offre d'emploi existante"""
        for i, posting in enumerate(self.active_postings):
            if posting.id == posting_id:
                updated_posting = builder.build()
                updated_posting.id = posting_id
                updated_posting.created_at = posting.created_at
                updated_posting.updated_at = datetime.now()
                self.active_postings[i] = updated_posting
                return updated_posting
        return None
    
    def remove_job_posting(self, posting_id: int) -> bool:
        """Supprime une offre d'emploi"""
        for i, posting in enumerate(self.active_postings):
            if posting.id == posting_id:
                del self.active_postings[i]
                return True
        return False
    
    def get_active_postings(self) -> List[JobPosting]:
        """Retourne toutes les offres d'emploi actives"""
        return [posting for posting in self.active_postings if posting.is_active()]
    
    def get_job_postings_by_company(self, company_id: int) -> List[JobPosting]:
        """Retourne toutes les offres d'emploi d'une entreprise spécifique"""
        # Supposons que company_id est une propriété de Company
        return [posting for posting in self.active_postings if posting.company and getattr(posting.company, 'id', None) == company_id]
    
    def get_job_posting(self, posting_id: int) -> Optional[JobPosting]:
        """Retourne une offre d'emploi spécifique par son ID"""
        for posting in self.active_postings:
            if posting.id == posting_id:
                return posting
        return None