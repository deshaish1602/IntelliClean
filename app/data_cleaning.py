import pandas as pd

class DataCleaning:

    def handle_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        for col in df.columns:
            if df[col].dtype in ['float64', 'int64']:
                mean_val = round(df[col].mean())
                df[col].fillna(mean_val, inplace=True)
                df[col] = df[col].round(0).astype(int)
            else:
                df[col].fillna(df[col].mode()[0] if not df[col].mode().empty else "Unknown", inplace=True)
        return df

    def remove_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:
        return df.drop_duplicates()

    def fix_data_types(self, df: pd.DataFrame) -> pd.DataFrame:
        for col in df.columns:
            try:
                converted = pd.to_numeric(df[col], errors='coerce')
                if converted.notna().all():
                    df[col] = converted.round(0).astype(int)
            except:
                pass
        return df

    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        df = self.handle_missing_values(df)
        df = self.remove_duplicates(df)
        df = self.fix_data_types(df)
        return df
