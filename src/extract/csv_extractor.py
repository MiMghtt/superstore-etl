import os
import pandas as pd


class CSVExtractor:

    def __init__(self, file_path: str, encoding: str = "utf-8"):
        self.file_path = file_path
        self.encoding = encoding

    def extract(self) -> pd.DataFrame:

        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Arquivo '{self.file_path}' não encontrado.")

        return pd.read_csv(self.file_path, encoding=self.encoding)
