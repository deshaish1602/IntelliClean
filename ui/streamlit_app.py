import streamlit as st
import pandas as pd
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.data_cleaning import DataCleaning

st.set_page_config(page_title="IntelliClean", page_icon="🧹", layout="wide")
st.title("🧹 IntelliClean — AI Data Cleaning Pipeline")
st.markdown("Upload your messy dataset and get it cleaned instantly.")

cleaner = DataCleaning()

tab1, tab2 = st.tabs(["Upload File", "About"])

with tab1:
    uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])
    if uploaded_file:
        st.subheader("Raw data")
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.info(f"Total rows: {len(df)} | Total columns: {len(df.columns)}")
        st.dataframe(df, use_container_width=True)

        if st.button("Clean this data"):
            with st.spinner("Cleaning your data..."):
                df_cleaned = cleaner.clean(df)

            st.success(f"Done! {len(df)} rows → {len(df_cleaned)} rows after cleaning")
            st.subheader("Cleaned data")
            st.dataframe(df_cleaned, use_container_width=True)

            col1, col2 = st.columns(2)
            with col1:
                st.metric("Original rows", len(df))
                st.metric("Original columns", len(df.columns))
            with col2:
                st.metric("Cleaned rows", len(df_cleaned))
                st.metric("Duplicates removed", len(df) - len(df_cleaned))

            csv = df_cleaned.to_csv(index=False)
            st.download_button(
                label="Download cleaned CSV",
                data=csv,
                file_name="intelliclean_cleaned.csv",
                mime="text/csv"
            )

with tab2:
    st.subheader("About IntelliClean")
    st.markdown("""
    ### What this app does
    - Handles missing values automatically
    - Removes duplicate rows
    - Fixes data types
    - Works with CSV and Excel files

    ### How missing values are handled
    - **Numeric columns** → filled with mean value
    - **Text columns** → filled with most common value

    ### Tech Stack
    - Python
    - Streamlit
    - Pandas
    - SQLAlchemy
    """)
