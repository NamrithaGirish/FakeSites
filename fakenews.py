import streamlit as st 
import joblib 

#load the joblib model 
model_nb = joblib.load('fake-news')

#user input 
st.title("SPAM HAM CLASSIFICATION")
ip = st.text_input("Enter your message:")

#predict if the entered message is spam or ham 
op = model_nb.predict([ip])
if st.button('PREDICT'):
  st.title(op[0])  #prints the output as spam or ham
