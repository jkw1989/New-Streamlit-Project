import streamlit as st

from Forms.contact import contact_form

@st.dialog("Contact Me")
def show_contact_form():
    contact_form()


#Hero Section

col1, col2 = st.columns(2, gap="small",vertical_alignment="center")
with col1:
    st.image("Assets/1597889965340.png", width=200)
with col2:
    st.title("James Wood",anchor=False)
    st.write("Data Visualization Design Engineer @ The Kraft Heinz Company | Tableau, Power BI, Design, Data Visualization")
    if st.button("📪 Contact Me"):
        show_contact_form()


#Experience and Qualifications
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - Tableau creator and breaker
    - Power BI wrangler
    - Data Visualization design and development
    - Being a team player!
    - Other cool stuff!
    """
)

st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - Engineering: Tableau, Power BI DAX, SQL, Streamlit?
    - Data Visualization: Tableau, Power BI, Figma, RAW Graphs
    - Miscelaneous: wood working and skiiing?
    - The soft stuff: Hard work?
    """
)
