>alembic init alembic

alembic.ini
```
sqlalchemy.url = sqlite:////home/souren/Code/Souren_pvt/Project_p/fastapi_clean_arch/config/sqlite/tmp_dbs/tmp.db
```
albemic/env.py
```
from src.infra.db_models.db_base import Base
from src.infra.db_models.user_db_model import User, Token
target_metadata = Base.metadata
```
>alembic revision --autogenerate -m "Adding UserDBModel"
>alembic upgrade head