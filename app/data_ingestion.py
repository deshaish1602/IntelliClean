import pandas as pd
from sqlalchemy import create_engine
import requests

class DataIngestion:

    def load_csv(self, filepath: str) -> pd.DataFrame:
        return pd.read_csv(filepath)

    def load_excel(self, filepath: str) -> pd.DataFrame:
        return pd.read_excel(filepath)

    def load_from_db(self, query: str, db_url: str) -> pd.DataFrame:
        engine = create_engine(db_url)
        return pd.read_sql(query, engine)

    def load_from_api(self, url: str) -> pd.DataFrame:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return pd.DataFrame(data)
