print("hello")

import streamlit as st
import google.generativeai as genai
st.title("SENTIMENT ANALYSIER")

text=st.text_area("enter your sentiment")
click=st.button("analyse")
if click:
    genai.configure(api_key="AIzaSyAaA2z8clwJWN8Iwa-3O_WydZVAPyD2RgA")
    model=genai.GenerativeModel("gemini-1.5-flash")
    response=model.generate_content(f"analyse sentiment of user text{text}")
    st.write(response.text)