import pandas as pd 
import streamlit as st
import plotly.express as px



st.title("New Sales Dashboard")
#st.markdown("_Prototype 10-10-24")

@st.cache_data
def load_data(file):
    data = pd.read_excel(file)
    return data

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is None:
    st.info(":rage:  Upload a file!")
    st.stop()

clean_data = pd.read_csv(uploaded_file)
st.write(clean_data)

chart_data = pd.DataFrame(uploaded_file)


st.line_chart(pd.read_csv("data/New Financial Data.csv"), x="Month", y="Sales", x_label=None, y_label=None, color=None, width=500, height=None, use_container_width=True)


