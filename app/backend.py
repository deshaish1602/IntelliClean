import pandas as pd
import io
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from app.data_cleaning import DataCleaning
from app.data_ingestion import DataIngestion
from app.database import get_engine

app = FastAPI(title="IntelliClean API")

cleaner = DataCleaning()
ingestion = DataIngestion()

@app.get("/")
def root():
    return {"message": "IntelliClean API is running"}

@app.post("/clean/upload")
async def clean_uploaded_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        if file.filename.endswith(".csv"):
            df = pd.read_csv(io.BytesIO(contents))
        elif file.filename.endswith((".xlsx", ".xls")):
            df = pd.read_excel(io.BytesIO(contents))
        else:
            raise HTTPException(status_code=400, detail="Only CSV and Excel files supported")

        original_rows = len(df)
        df_cleaned = cleaner.clean(df)

        engine = get_engine()
        df_cleaned.to_sql("cleaned_data", engine, if_exists="replace", index=False)

        return JSONResponse({
            "status": "success",
            "original_rows": original_rows,
            "cleaned_rows": len(df_cleaned),
            "columns": list(df_cleaned.columns),
            "preview": df_cleaned.to_dict(orient="records")
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/clean/db")
def clean_from_db(query: str = "SELECT * FROM cleaned_data"):
    try:
        engine = get_engine()
        df = pd.read_sql(query, engine)
        df_cleaned = cleaner.clean(df)
        return JSONResponse({
            "status": "success",
            "rows": len(df_cleaned),
            "preview": df_cleaned.to_dict(orient="records")
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
