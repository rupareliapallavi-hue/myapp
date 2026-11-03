import streamlit as st          
st.title("area calculator website")
st.subheader("rectangle")
length=st.number_input("enter length")
breath=st.number_input("enter breath")
if st.button("area of rectangle"):
    r=0
    r=length*breath
    st.write(r)


st.subheader("area of square")
side=st.number_input("enter side")
if st.button("area of square"):
    s=0
    s=side*side
    st.write(s)


st.subheader("area of triangle")
base=st.number_input("enter base")
height=st.number_input("enter height")
if st.button("area of triangle"):
    t=0
    t=1/2*base*height
    st.write(t)


st.subheader("area of circle")
radius=st.number_input("enter radius")
if st.button("area of circle"):
    c=0
    c=3.141592653589793238462643383279502884197*radius*radius
    st.write(c)