import pandas as pd
import streamlit as st 



# --- Page Setup 

st.set_page_config(layout="centered")


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

# --- Navigation

pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page, project_3_page],
    }
)

st.logo("Assets/Screenshot 2024-10-09 at 9.12.22 PM.png")
#st.sidebar.text("Made with 💖 by me")

pg.run()