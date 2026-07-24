from src.extract.csv_extractor import CSVExtractor
from src.extract.csv_extractor import CSVExtractor
from src.transform.data_normalizer import DataNormalizer
from src.database.database_connection import DatabaseConnection
from src.load.database_loader import DatabaseLoader


def main():
    extractor = CSVExtractor(
        file_path=r"data\raw\Sample - Superstore.csv", encoding="latin-1"
    )
    df = extractor.extract()
    print(df.head())

    normalizer = DataNormalizer(df)

    tables = normalizer.normalize()

    engine = DatabaseConnection.get_engine()
    try:
        with engine.connect() as conn:
            print("Conectado com sucesso!")
    except Exception as e:
        print(type(e))
        print(e)

    loader = DatabaseLoader(engine)

    for table_name, dataframe in tables.items():
        loader.load(dataframe, table_name)


if __name__ == "__main__":
    main()
