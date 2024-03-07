from abc import ABC
from pydantic import BaseModel

class MetaDataBase(BaseModel, ABC):
    id: str
    created_at: str
    update_at: str


