from app.data_ingestion import DataIngestion
from app.data_cleaning import DataCleaning
from app.ai_agent import ai_clean
from app.database import get_engine

def run_pipeline(filepath: str):
    print("=== IntelliClean Pipeline Starting ===")
    ingestion = DataIngestion()
    cleaner = DataCleaning()
    df = ingestion.load_csv(filepath)
    print(f"Loaded {len(df)} rows")
    df_cleaned = cleaner.clean(df)
    print(f"After cleaning: {len(df_cleaned)} rows")
    engine = get_engine()
    df_cleaned.to_sql("cleaned_data", engine, if_exists="replace", index=False)
    print("Saved to SQLite database")
    sample_text = df_cleaned.head(5).to_string()
    ai_result = ai_clean(sample_text)
    print(f"\nAI Agent Output:\n{ai_result}")
    print("\n=== Pipeline Complete ===")
    print(df_cleaned)

if __name__ == "__main__":
    run_pipeline("data/sample.csv")
