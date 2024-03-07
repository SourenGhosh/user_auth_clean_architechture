
from abc import ABCMeta
from sqlalchemy.exc import IntegrityError
from src.interactor.errors.error_classes import UniqueViolationError

from src.interactor.interfaces.repositories.user_repository import UserRepositoryInterface
from src.infra.db_models.db_base import Session
from src.domain.user.user import UserInfo
from src.infra.db_models.user_db_model import User

class UserSqlRepositories(UserRepositoryInterface):
    def __init__(self) -> None:
        self.__session = Session
    
    def register_user(self, user_form) -> UserInfo:
        
        _user = User(**user_form.dict())
        try:
            self.__session.add(_user)
            self.__session.commit()
            self.__session.refresh(_user)
        except IntegrityError as e:
            if "violates unique constraint" in str(e.orig):
                raise UniqueViolationError(
                    "Profession with the same name already exists"
                ) from e
            raise
        
        

