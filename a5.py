import streamlit as st
import google.generativeai as genai
api_Key ="AIzaSyCQrpvKrSnHCwbIKhl2OncdWzrk3n_zYkQ"
model=genai.GenerativeModel("gemini-1.5-flash")

st.title("AI-Powered chatbot for interview preparation")
select=st.selectbox("pick one",["python","machine learning","data science"])
click=st.button("search")
if click:
   genai.configure(api_key="AIzaSyCQrpvKrSnHCwbIKhl2OncdWzrk3n_zYkQ") 
   model=genai.GenerativeModel("gemini-1.5-flash")
   response=model.generate_content(f"ask relevant interview question and evaluate users responses")
   st.feedback("thumbs")
   st.write(response.text)