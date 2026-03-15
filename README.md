# IntelliClean — AI Powered Data Cleaning Pipeline

An end-to-end automated data cleaning system built with FastAPI, Streamlit, LangChain and SQLite.

## Features
- Upload CSV and Excel files
- Automatic missing value handling
- Duplicate removal
- Data type fixing
- REST API built with FastAPI
- Interactive UI built with Streamlit
- SQLite database integration

## Tech Stack
- Python
- FastAPI
- Streamlit
- Pandas
- LangChain
- SQLite
- SQLAlchemy

## How to Run

### 1. Clone the repo
git clone https://github.com/yourusername/IntelliClean.git
cd IntelliClean

### 2. Create virtual environment
/usr/bin/python3 -m venv venv
source venv/bin/activate

### 3. Install packages
pip install -r requirements.txt

### 4. Run FastAPI backend
uvicorn app.backend:app --reload

### 5. Run Streamlit UI
streamlit run ui/streamlit_app.py

### 6. Open browser
http://localhost:8501
