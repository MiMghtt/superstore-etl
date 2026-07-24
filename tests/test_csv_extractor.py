import pandas as pd
import pytest

from src.extract.csv_extractor import CSVExtractor


def test_extract_returns_dataframe():

    extractor = CSVExtractor(
        "data/raw/Sample - Superstore.csv",
        encoding="latin-1"
    )

    df = extractor.extract()

    assert isinstance(df, pd.DataFrame)


def test_extract_returns_rows():

    extractor = CSVExtractor(
        "data/raw/Sample - Superstore.csv",
        encoding="latin-1"
    )

    df = extractor.extract()

    assert len(df) > 0


def test_file_not_found():

    extractor = CSVExtractor(
        "arquivo_inexistente.csv"
    )

    with pytest.raises(FileNotFoundError):
        extractor.extract()