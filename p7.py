import streamlit as st    
st.title("Math Quiz")
st.subheader("Q1 3+2=?")
q1=st.radio("options",["5","6","10","11"])
st.subheader("Q2 5+5=?")
q2=st.radio("options",["9","6","10","11"])
st.subheader("Q3 6+5=?")
q3=st.radio("options",["5","13","10","11"])
st.subheader("Q4 11+6=?")
q4=st.radio("options",["17","13","15","11"])
st.subheader("Q5 7+14=?")
q5=st.radio("opinions",["17","13","21","19"])
st.subheader("Q6 9+11=?")
q6=st.radio("options",["17","13","20","11"])
st.subheader("Q7 12+6=?")
q7=st.radio("options",["18","13","10","11"])
if st.button("submit"):
    s=0
    if q1=="5":
        s=s+1
    else:
        st.write("In q1 your answer is wrong the right answer is 5")
    if q2=="10":
        s=s+1
    else:
        st.write("In q2 your answer is wrong the right answer is 10")
    if q3=="11":
        s=s+1
    else:
        st.write("In q3 your answer is wrong the right answer is 11")
    if q4=="17":
        s=s+1
    else:
        st.write("In q4 your answer is wrong the right answer is 17")
    if q5=="21":
        s=s+1
    else:
        st.write("In q5 your answer is wrong the right answer is 21")
    if q6=="20":
        s=s+1
    else:
        st.write("In q6 your answer is wrong the right answer is 20")
    if q7=="18":
        s=s+1
    else:
        st.write("In q7 your answer is wrong the right answer is 18")
    st.write(s) 