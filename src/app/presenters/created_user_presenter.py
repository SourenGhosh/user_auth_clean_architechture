from typing import Dict

from src.interactor.interfaces.presenters.created_user_presenter import CreateUserPresenterInterface

class CreatedUserPresenter(CreateUserPresenterInterface):
    """
        class to show created user details
    """
    def show_register_user(self, output) -> Dict:
        return output
    
