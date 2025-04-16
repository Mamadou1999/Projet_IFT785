# Interface ProfileDecorator
from abc import ABC, abstractmethod
from typing import Dict, Any

class ProfileDecorator(ABC):
    def __init__(self, user):
        self.user = user
    
    @abstractmethod
    def get_profile(self) -> Dict[str, Any]:
        pass
