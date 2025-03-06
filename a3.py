print("hello")

import streamlit as st
st.title("TRAVEL ITINERARY GENERATOR")
import google.generativeai as genai
 
destination=st.text_area("enter destination")
duration=st.text_input("enter duration")
click=st.button("generate travell itinerary")
if click:
    genai.configure(api_key="AIzaSyAaA2z8clwJWN8Iwa-3O_WydZVAPyD2RgA")
    model=genai.GenerativeModel("gemini-1.5-flash")
    response=model.generate_content(f"generate travel itineray based on destination{destination}and duration{duration}and give information about food, recommend activities ")
    st.write(response.text)
