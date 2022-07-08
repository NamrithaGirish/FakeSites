import streamlit as st
import joblib
model=joblib.load('fake-news')
st.title("FAKE SITE DETECTOR")
ip=st.text_input("WEBSITE NAME")
op=model.predict([ip])
if st.button("CHECK"):
  if op[0]==0:
    st.title("FAKE NEWS")
  else :
    st.title("GENUINE NEWS")
   
