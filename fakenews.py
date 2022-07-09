import streamlit as st 
import joblib 

#LOADING JOBLIB MODEL 
model = joblib.load('fake-news')

#user input 
st.title("FAKE NEWS WEBSITE DETECTOR")
ip = st.text_input("ENTER WEBSITE URL/ NAME")

#MODIFYING INPUT
inpt =''
for i in ip:
  if i.isspace():
    continue
  else:
    inpt+=i

#PREDIVTING LEGITIMACY OF SITE 
op = model.predict([inpt])
if st.button('CHECK'):
  if op[0]==0:
    st.header("FAKE NEWS WEBSITE")
  else:
    st.header("LEGITIMATE NEWS WEBSITE")  
