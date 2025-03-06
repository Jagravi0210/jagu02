print("hello")

import streamlit as st
st.title("RESUME GENERATOR")
import google.generativeai as genai
name=st.text_area("enter name")
skills=st.text_area("enter skills")
experience=st.text_area("enter experience")
education=st.text_area("enter education")
click=st.button("generate resume")
if click:
    genai.configure(api_key="AIzaSyAaA2z8clwJWN8Iwa-3O_WydZVAPyD2RgA")
    model=genai.GenerativeModel("gemini-1.5-flash")
    response=model.generate_content(f"generate resume based on name{name}and skills{skills},experience{experience},and education{education}")
    st.write(response.text)