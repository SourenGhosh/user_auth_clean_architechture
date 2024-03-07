from typing import Dict
from abc import ABC, abstractmethod

class FastAPIUserControllerInterface(ABC):
    """
        This is interface of user controller
    """

    def get_user_info(self, input) -> None:
        """
        """
    
    @abstractmethod
    def hide_user_metadata(self, user):
        """
        """