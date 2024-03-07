from sqlalchemy import TIMESTAMP, Column, Integer, text, String
from src.infra.db_models.db_base import Base

class AbstractModel(Base):
    """Base Models

    Args:
        Base (_type_): Inherits Base from SQLAlchemy and specifies columns for inheritance.
    """

    __abstract__ = True

    id = Column(Integer, nullable=False, primary_key=True)
    created_at = Column(String, server_default="2021-01-01")
    updated_at = Column(String, server_default="2021-01-01")