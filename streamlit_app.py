import streamlit as st 

st.title("New Multi Page App")

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

# --- Navigation

pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page],
    }
)



pg.run()