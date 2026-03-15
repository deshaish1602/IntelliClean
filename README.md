# IntelliClean — AI Powered Data Cleaning Pipeline

IntelliClean is an end-to-end automated data cleaning system that combines rule-based preprocessing with AI-assisted reasoning to clean messy datasets from multiple sources. The project provides a complete pipeline with a REST API backend, an interactive UI, and database integration for storing cleaned datasets.

The system is designed to simulate a real-world data engineering workflow where raw data from CSV/Excel files is automatically cleaned, validated, and prepared for analytics or machine learning pipelines.

---

## Key Features

- Upload CSV and Excel datasets through an interactive UI
- Automated handling of missing values
- Duplicate row detection and removal
- Automatic data type correction
- AI-assisted data cleaning using LangChain
- RESTful API service built with FastAPI
- Interactive data interface built with Streamlit
- Local database storage using SQLite
- Modular architecture for ingestion, cleaning, and storage
- Scalable pipeline design suitable for real-world datasets

---

## Project Architecture

The system follows a modular pipeline architecture:

User Upload → Data Ingestion → Data Cleaning → AI Processing → Database Storage → Clean Output

Components include:

- **FastAPI Backend**  
  Handles API endpoints, dataset ingestion, and cleaning pipeline execution.

- **Streamlit Frontend**  
  Provides an interactive UI for uploading datasets and viewing cleaned outputs.

- **Data Cleaning Module**  
  Uses Pandas and NumPy to apply rule-based preprocessing such as missing value imputation and duplicate removal.

- **AI Agent (LangChain)**  
  Enhances preprocessing by analyzing dataset structure and suggesting intelligent cleaning strategies.

- **SQLite Database**  
  Stores processed datasets and enables simple querying without requiring a separate database server.

---

## Tech Stack

- Python
- FastAPI
- Streamlit
- Pandas
- NumPy
- LangChain
- SQLite
- SQLAlchemy
- Uvicorn

---

## Project Structure

IntelliClean/
│
├── app/
│   ├── backend.py
│   ├── data_cleaning.py
│   ├── data_ingestion.py
│   └── ai_agent.py
│
├── ui/
│   └── streamlit_app.py
│
├── data/
│   └── sample_datasets
│
├── database/
│   └── database.py
│
├── requirements.txt
└── README.md

---

## How to Run

### 1. Clone the repository
git clone https://github.com/yourusername/IntelliClean.git  
cd IntelliClean

### 2. Create virtual environment
/usr/bin/python3 -m venv venv  
source venv/bin/activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run FastAPI backend
uvicorn app.backend:app --reload

### 5. Run Streamlit UI
streamlit run ui/streamlit_app.py

### 6. Open browser
http://localhost:8501

---

## Example Workflow

1. Upload a CSV or Excel dataset through the Streamlit interface
2. The file is sent to the FastAPI backend
3. The backend performs:
   - Missing value handling
   - Duplicate removal
   - Data type correction
4. Optional AI processing enhances cleaning strategies
5. Cleaned data is stored in SQLite
6. Results are displayed in the Streamlit UI

---

## Use Cases

- Preparing messy datasets for machine learning
- Automating repetitive data preprocessing tasks
- Building data engineering pipelines
- Demonstrating AI-assisted data cleaning workflows
- Educational projects for data science and AI systems

---

## Future Improvements

- Support for PostgreSQL and cloud databases
- Automated data validation rules
- Data profiling dashboard
- Docker containerization
- Deployment on cloud platforms
- Support for API-based data ingestion

---

## Author

Aishwarya Deshwal  
B.Tech Computer Science Engineering  
Bennett University


