from sqlalchemy import Boolean, Column, ForeignKey, String, text
from sqlalchemy.orm import relationship

from src.infra.db_models.db_abstract import AbstractModel

class User(AbstractModel):
    __tablename__ = "users"
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True)
    password = Column(String, nullable=False)
    is_verified = Column(Boolean, nullable=False, server_default=text("false"))

class Token(AbstractModel):
    __tablename__ = "user_token"
    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    token = Column(String, nullable=False)
    user = relationship("User", passive_deletes=True)
    