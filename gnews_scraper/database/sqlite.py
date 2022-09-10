from typing import Optional

import sqlalchemy
from sqlalchemy.engine import Engine


def connect_sqlite(file_path: Optional[str] = None) -> Engine:

    if file_path:
        connection_uri = "sqlite:///%s" % (file_path)
    else:
        connection_uri = "sqlite://"

    engine = sqlalchemy.create_engine(connection_uri)

    return engine
