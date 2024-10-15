import streamlit as st
import pandas as pd
from pygwalker.api.streamlit import StreamlitRenderer
from streamlit_extras.add_vertical_space import add_vertical_space



st.title("Tableau Alternative")

st.subheader("This is a way to ")

add_vertical_space(5)
df = pd.read_csv("data/New Financial Data.csv")
pyg_app = StreamlitRenderer(df)
pyg_app.explorer()