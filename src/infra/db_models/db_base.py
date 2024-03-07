from sqlalchemy.orm import DeclarativeBase, sessionmaker, scoped_session
from sqlalchemy import create_engine
from config.sqlite.sqlite_client_config import SQLiteClientConfig

class Base(DeclarativeBase):
    """ Base class for all models
    """
    pass
client_config = SQLiteClientConfig(r"sqlite:////home/souren/Code/Souren_pvt/Project_p/fastapi_clean_arch/config/sqlite/tmp_dbs/tmp.db")
engine = create_engine(client_config.url)
Session = scoped_session(sessionmaker(bind=engine))


