import pandas as pd 
import streamlit as st
import duckdb as db 


st.title("New Sales Dashboard")
st.markdown("_Prototype 10-10-24")

@st.cache_data
def load_data(file):
    data = pd.read_excel(file)
    return data

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is None:
    st.info(":rage: Upload a file!")
    st.stop()

df = load_data(uploaded_file)
st.dataframe(
    df,
    column_config={
        "Year": st.column_config.NumberColumn(format="%d")
    })
