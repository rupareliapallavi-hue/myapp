import streamlit as st 
st.title("registration form")
birthdate=st.date_input("date of birth")
email=st.text_input("put your email")
password=st.text_input("password")
gender=st.radio("select your gender", ["male","female"])
running=st.checkbox("running")
play=st.checkbox("playing")
address=st.text_area("put your address")
st.button("Register")
    