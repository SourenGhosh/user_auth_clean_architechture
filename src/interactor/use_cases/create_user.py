from typing import Dict, Optional

from src.interactor.interfaces.logger.logger import LoggerInterface
from src.interactor.errors.error_classes import ItemNotCreatedException

from src.interactor.interfaces.presenters.created_user_presenter import CreateUserPresenterInterface
from src.interactor.interfaces.repositories.user_repository import UserRepositoryInterface

from src.domain.user.user import InputUser

class CreateUserUseCase():
    """
        Responsible for creating new user
    """
    def __init__(
            self,
            presenter: CreateUserPresenterInterface,
            repository: UserRepositoryInterface,
            logger: Optional[LoggerInterface] = None
            ) -> None:
        self.presenter = presenter
        self.repository = repository
        self.logger = logger

    def create_user(self, InputUser):
        self.repository.register_user(InputUser)

    
        
        


