import streamlit as st 
import joblib 

#load the joblib model 
model_nb = joblib.load('fake-news')

#user input 
st.title("FAKE NEWS SITE DETECTOR")
ip = st.text_input("ENTER WEBSITE URL/ NAME")

#predict legitimacy of website 
op = model_nb.predict([ip])
if st.button('CHECK'):
  if op[0]==0:
    st.title("FAKE WEBSITE")
  else:
    st.title("LEGITIMATE WEBSITE")  
