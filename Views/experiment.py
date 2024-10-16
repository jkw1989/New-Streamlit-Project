import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_extras.metric_cards import style_metric_cards


iris_df = px.data.iris()
st.title("Iris Dataset")

#---- KPI
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="My Metric!",value="75%",delta="-1,5%")
    style_metric_cards(border_color="FFFFF", border_size_px=3)

with col2:
    st.metric(label="My Metric!",value="75%",delta="1,5%")

with col3:
    st.metric(label="My Metric!",value="75%",delta="-1,5%")




st.divider()

#---- Interactive Chart
#chart selection

st.subheader("Customizable Charts!")

col1, col2, col3 = st.columns(3)

with col1:
    x_axis = st.selectbox("Choose a varable for the x axis",iris_df.columns,index=0)
with col2: 
    y_axis = st.selectbox("Choose a varable for the y axis",iris_df.columns,index=1)
with col3:
    chart_type = st.selectbox("Select chart type:",("Scatter Plot", "Line Chart","Bar Chart"))

if chart_type == "Scatter Plot":
    colored_bubble_hover_fig = px.scatter(iris_df,x=x_axis,y=y_axis,color="species", size="sepal_length",size_max=6,opacity=.75,trendline="ols")
    st.plotly_chart(colored_bubble_hover_fig)
elif chart_type == "Line Chart":
    iris_df_sorted = iris_df.sort_values(by="sepal_length").reset_index()
    fig = px.line(iris_df_sorted, x=iris_df_sorted.index,y=y_axis,color="species",title="Iris Sepal Length Line Chart")
    st.plotly_chart(fig)
elif chart_type == "Bar Chart":
    avg_sepal_length = iris_df.groupby("species")["sepal_length"].mean().reset_index()
    fig = px.bar(avg_sepal_length, x = "species", y = "sepal_length", title="Avg Sepal Lengh")
    st.plotly_chart(fig)



#st.dataframe(iris_df)

simple_container = st.container(border=True)
simple_container.write("This is inside the container")
simple_container.dataframe(iris_df)


#tabs

st.subheader("Tabs are fun!")

tab1, tab2, tab3 = st.tabs(["bubble chart","line chart","bar chart"])

with tab1:
    colored_bubble_hover_fig_1 = px.scatter(iris_df,x=x_axis,y=y_axis,color="species", size="sepal_length",size_max=6,opacity=.75)
    st.plotly_chart(colored_bubble_hover_fig_1)
with tab2: 
    iris_df_sorted = iris_df.sort_values(by="sepal_length").reset_index()
    fig = px.line(iris_df_sorted, x=iris_df_sorted.index,y=y_axis,color="species",title="Iris Sepal Length Line Chart")
    st.plotly_chart(fig)
with tab3:
    avg_sepal_length = iris_df.groupby("species")["sepal_length"].mean().reset_index()
    fig = px.bar(avg_sepal_length, x = "species", y = "sepal_length", title="Avg Sepal Lengh")
    st.plotly_chart(fig)

