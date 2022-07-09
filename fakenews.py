import streamlit as st 
import joblib 

#load the joblib model 
model = joblib.load('fake-news')

#user input 
st.title("FAKE NEWS WEBSITE DETECTOR")
ip = st.text_input("ENTER WEBSITE URL/ NAME")

#modifying input
inpt =''
for i in ip:
  if i.isspace():
    continue
  else:
    inpt+=i

#predict legitimacy of website 
op = model.predict([inpt])
if st.button('CHECK'):
  if op[0]==0:
    st.header("FAKE WEBSITE")
  else:
    st.header("LEGITIMATE WEBSITE")  
