import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:8000"

st.set_page_config(page_title="IntelliClean", page_icon="🧹", layout="wide")
st.title("🧹 IntelliClean — AI Data Cleaning Pipeline")
st.markdown("Upload your messy dataset and get it cleaned instantly.")

tab1, tab2 = st.tabs(["Upload File", "Query Database"])

with tab1:
    uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])
    if uploaded_file:
        st.subheader("Raw data preview")
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.info(f"Total rows in uploaded file: {len(df)}")
        st.dataframe(df, use_container_width=True)

        if st.button("Clean this data"):
            uploaded_file.seek(0)
            with st.spinner("Cleaning..."):
                response = requests.post(
                    f"{API_URL}/clean/upload",
                    files={"file": (uploaded_file.name, uploaded_file, "multipart/form-data")}
                )
            if response.status_code == 200:
                result = response.json()
                st.success(f"Cleaned! {result['original_rows']} → {result['cleaned_rows']} rows")

                cleaned_df = pd.DataFrame(result["preview"])

                st.subheader(f"Cleaned data — {len(cleaned_df)} rows")
                st.dataframe(cleaned_df, use_container_width=True)

                csv = cleaned_df.to_csv(index=False)
                st.download_button(
                    label="Download complete cleaned CSV",
                    data=csv,
                    file_name="intelliclean_cleaned.csv",
                    mime="text/csv"
                )
            else:
                st.error(f"Error: {response.text}")

with tab2:
    query = st.text_input("SQL Query", value="SELECT * FROM cleaned_data")
    if st.button("Run Query"):
        with st.spinner("Fetching..."):
            response = requests.get(f"{API_URL}/clean/db", params={"query": query})
        if response.status_code == 200:
            result = response.json()
            cleaned_df = pd.DataFrame(result["preview"])
            st.success(f"{result['rows']} rows returned")
            st.dataframe(cleaned_df, use_container_width=True)

            csv = cleaned_df.to_csv(index=False)
            st.download_button(
                label="Download complete cleaned CSV",
                data=csv,
                file_name="intelliclean_cleaned.csv",
                mime="text/csv"
            )
        else:
            st.error(f"Error: {response.text}")
