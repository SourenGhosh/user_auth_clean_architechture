from typing import List
from fastapi import APIRouter, Depends, status, Request
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from fastapi import FastAPI

from src.app.controller.user_controller import UserController
from src.domain.user.user import InputUser, UserInfo

class UserRestApi(FastAPI):
    def __init__(self, user_controller: UserController):
        super().__init__()
    
        @self.post("/api/v1/register-user")
        def register_user(inputUser: InputUser):
            return user_controller.create_user(inputUser)