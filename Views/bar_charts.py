import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_extras.add_vertical_space import add_vertical_space

iris_df = px.data.iris()

st.title("Bar Charts")
st.markdown("Bar charts display data using (you guessed it) bars that are proportional to the values they represent. There are several different types of bar charts depending on the data and the story the chart is telling. Bar chart data is categorical and answers the question “how many” are in each category.")
st.link_button("View more in Delish!", "https://delish.supernova-docs.io/latest/data-visualization/chart-guidelines/bar-yNxnO53Z")

add_vertical_space(5)

#data_file =  pd.read_csv("data/New Financial Data.csv")

chart_data = pd.DataFrame(data = iris_df)
summarized =  pd.DataFrame.describe(chart_data)

st.dataframe(summarized)


st.bar_chart(data=chart_data, x="species",y="sepal_width",height=600,x_label="Species",y_label="Sepal Width", color="species")