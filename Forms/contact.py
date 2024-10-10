import streamlit as st 

with st.form("contact form"):
    name = st.text_input("First Name")
    email = st.text_input("Email Adress")
    message = st.text_area("Your Message")
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        st.success("Message successfully send!")