from typing import Dict
from abc import ABC, abstractmethod

class CreateUserPresenterInterface(ABC):
    """
        Class for the interface of the UserPresenter
    """

    @abstractmethod
    def show_register_user(self, output) -> Dict:
        """
            Show created user
        """