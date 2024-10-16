import pandas as pd
import streamlit as st
import numpy as np 
import plotly.express as px 
from streamlit_extras.add_vertical_space import add_vertical_space



st.title("Line Charts")

df = pd.DataFrame(np.random.randn(10,2),columns = ["prices","diff"])
col1, col2, col3 = st.columns(3)

col1.line_chart(df)
col2.line_chart(df,y="diff")

add_vertical_space(2)

st.divider()

add_vertical_space(2)

st.line_chart(df,y="diff",height=200,width=100)

st.area_chart(df)