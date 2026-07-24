import pandas as pd
from sqlalchemy import create_engine

from src.load.database_loader import (
    DatabaseLoader
)


def test_load_table():

    engine = create_engine(
        "sqlite:///:memory:"
    )

    loader = DatabaseLoader(engine)

    df = pd.DataFrame(
        {
            "id": [1, 2],
            "name": ["A", "B"]
        }
    )

    loader.load(
        dataframe=df,
        table_name="test_table"
    )

    loaded_df = pd.read_sql(
        "SELECT * FROM test_table",
        engine
    )

    assert len(loaded_df) == 2