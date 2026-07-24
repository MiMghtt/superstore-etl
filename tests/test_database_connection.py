from sqlalchemy.engine import Engine

from src.database.database_connection import (
    DatabaseConnection
)


def test_get_engine():

    engine = DatabaseConnection.get_engine()

    assert isinstance(engine, Engine)
