import streamlit as st 

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(label="My Metric!",value="75%",delta="-1,5%")
col2.metric(label="My Metric!",value="50%",delta="1,5%")
col3.metric(label="My Metric!",value="10%",delta="-10,5%")
