import streamlit as st
no=st.number_input("enter number")      
if no%2 == 0:
    st.write("even")
else:
    st.write("odd")