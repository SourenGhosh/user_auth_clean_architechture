from abc import ABC, abstractmethod

from typing import Optional

from src.domain.user.user import InputUser
class UserRepositoryInterface(ABC):
    @abstractmethod
    def register_user(self, user: InputUser):
        """
            Register User
        """