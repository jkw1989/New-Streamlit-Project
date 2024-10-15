import pandas as pd
import streamlit as st 
import plotly.express as px


# --- Page Setup 




about_page = st.Page(
    page="Views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    page="Views/sales_dashboard.py",
    title="Sales Dashboard",
    icon=":material/bar_chart:",
)
project_2_page = st.Page(
    page="Views/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)
project_3_page = st.Page(
    page="Views/experiment.py",
    title="Experiments",
    icon=":material/experiment:",
)
project_4_page = st.Page(
    page="Views/tableau_alternative.py",
    title="Tableau Alternative",
    icon=":material/query_stats:",
)
project_5_page = st.Page(
    page="Views/bar_charts.py",
    title="Bar Charts",
    icon=":material/equalizer:",
)
project_6_page = st.Page(
    page="Views/line_charts.py",
    title="Line Charts",
    icon=":material/stacked_line_chart:",
)
project_7_page = st.Page(
    page="Views/tables.py",
    title="Tables",
    icon=":material/table_chart:",
)
project_8_page = st.Page(
    page="Views/scatter_chart.py",
    title="Scatter Plots",
    icon=":material/scatter_plot:",
)

# --- Navigation

pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page, project_3_page, project_4_page],
        "Charts": [project_5_page,project_6_page,project_7_page,project_8_page],
    }
)

st.logo("Assets/Screenshot 2024-10-09 at 9.12.22 PM.png")
st.sidebar.text("Made with 💖 by me")

pg.run()