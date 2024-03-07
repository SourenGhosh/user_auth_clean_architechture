from typing import Optional
class SQLiteClientConfig:

    def __init__(self,
                 conn_string: Optional[str] = None,
                ):
        self.url = conn_string
        