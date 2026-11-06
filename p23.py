import streamlit as st           
st.title("frequently used images")
st.image("2.jpg", width=400)
st.caption("TOM AND JERRY ")
col1, col2,col3 = st.columns(3)
with col1:
    st.image("3.jpg")
with col2:
    st.image("4.jpg")
with col3:
    st.image("5.jpg")
st.image("2.png",width=600)
st.caption("mythical gods")
col_1,col_2 = st.columns(2)
with col_1:
    st.image("1.png")
with col_2:
    st.image("6.jpg")
c1,c2,c3 = st.columns(3)
with c1:
    st.image("7.jpg")
with c2:
    st.image("8.jpg")
with c3:
    st.image("9.jpg")
r1,r2 = st.columns (2)
with r1:
    st.image("10.jpg")
with r2:
    st.image("11.jpg")