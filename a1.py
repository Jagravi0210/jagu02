print("hello")

import streamlit as st
st.title("code review and helper")
import google.generativeai as genai

code=st.text_area("enter your python code")
click=st.button("check the code.")
if click:
    genai.configure(api_key="AIzaSyAaA2z8clwJWN8Iwa-3O_WydZVAPyD2RgA")
    model=genai.GenerativeModel("gemini-1.5-flash")
    response=model.generate_content(f"check if the python{code}code is correct and if it is not correct help to find the error and give correct code.")
    st.write(response.text)