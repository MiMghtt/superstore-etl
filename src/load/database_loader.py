class DatabaseLoader:

    def __init__(self, engine):
        self.engine = engine

    def load(self, dataframe, table_name):

        dataframe.to_sql(
            name=table_name,
            con=self.engine,
            if_exists="replace",
            index=False
        )

        print(
            f"Tabela '{table_name}' carregada com sucesso."
        )