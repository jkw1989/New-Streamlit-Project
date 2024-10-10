import streamlit as st

#Hero Section

col1, col2 = st.columns(2, gap="small",vertical_alignment="center")
with col1:
    st.image("Assets/1597889965340.png", width=230)
with col2:
    st.title("James Wood",anchor=False)
    st.write("Data Visualization Design Engineer @ The Kraft Heinz Company | Tableau, Power BI, Design, Data Visualization")