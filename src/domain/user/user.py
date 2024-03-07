from src.domain.base.abstract_base import MetaDataBase
from pydantic import BaseModel

class UserInfo(MetaDataBase):
    first_name: str
    last_name: str
    email: str
    is_verified: bool = False

class InputUser(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
