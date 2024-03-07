from typing import Optional

from src.app.interfaces.user_sql_db_controller_interface import FastAPIUserControllerInterface
from src.interactor.interfaces.logger.logger import LoggerInterface

#infra/app
from src.infra.repositories.user_sql_repositories import UserSqlRepositories
from src.app.presenters.created_user_presenter import CreatedUserPresenter
#usecase
from src.interactor.use_cases.create_user import CreateUserUseCase

class UserController(FastAPIUserControllerInterface):
    def __init__(self, logger: Optional[LoggerInterface] = None) -> None:
        self.logger = logger
        repository = UserSqlRepositories()
        presenter = CreatedUserPresenter()
        self.use_case = CreateUserUseCase(presenter, repository)
    
    def get_user_info(self, input) -> None:
        return NotImplementedError
    
    def hide_user_metadata(self, user):
        return NotImplementedError
    
    def create_user(self, user):
        self.use_case.create_user(user)
        

    

    

