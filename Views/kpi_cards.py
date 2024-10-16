import streamlit as st 
from streamlit_extras.metric_cards import style_metric_cards

#with open('style.css') as f:
#    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(label="My Metric!",value="75%",delta="-1,5%")
col2.metric(label="My Metric!",value="50%",delta="1,5%")
col3.metric(label="My Metric!",value="10%",delta="-10,5%",delta_color="off")

st.divider()

col10, col11, col12 = st.columns(3)

col10.metric(label="Gain", value=5000, delta=1000)
col11.metric(label="Loss", value=5000, delta=-1000)
col12.metric(label="No Change", value=5000, delta=0)

#style_metric_cards(
#    background_color="#E6E6E6",
#    box_shadow="False",
#    border_left_color="blue",
#)