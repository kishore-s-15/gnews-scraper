import sqlalchemy
from sqlalchemy.engine import Engine


def connect_postgres(
    username: str, password: str, db_host: str, port: int, db_name: str
) -> Engine:

    engine = sqlalchemy.create_engine(
        "postgresql://%s:%s@%s:%d/%s" % (username, password, db_host, port, db_name)
    )

    return engine
