import streamlit as st
import pandas as pd
from pygwalker.api.streamlit import StreamlitRenderer

st.set_page_config(layout="wide")


st.title("Tableau Alternative")

uploaded_file = st.file_uploader ("your CSV data")



if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    pyg_app = StreamlitRenderer(df)
    pyg_app.explorer()