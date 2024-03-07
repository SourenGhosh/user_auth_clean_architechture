import uvicorn
from src.app.rest_apis.users_api import UserRestApi
from src.app.controller.user_controller import UserController

def start_application() -> UserRestApi:
    user_controller = UserController()
    user_rest_api = UserRestApi(user_controller=user_controller)
    return user_rest_api


if __name__ == "__main__":
    uvicorn.run(app=start_application())
    