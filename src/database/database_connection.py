from sqlalchemy import create_engine
from src.config.settings import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD


class DatabaseConnection:

    @staticmethod
    def get_engine():

        connection_string = (
            f"postgresql+psycopg2://"
            f"{DB_USER}:{DB_PASSWORD}"
            f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        )

        return create_engine(connection_string)
