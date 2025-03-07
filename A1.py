import streamlit as st
import google.cloud  as genai

st.title("Personalized Wardrobe App")
st.subheader("Get fashion recommendations, styling advice, and visual try-ons!")

# Simulated clothing images (replace with actual clothing images in 'images/' folder)
clothing_items = {
    'casual': ['outfit1.jpg', 'outfit2.jpg'],
    'formal': ['outfit3.jpg', 'outfit4.jpg'],
    'sportswear': ['outfit5.jpg', 'outfit6.jpg']
}

# Simple function for fashion recommendations based on style and occasion
def get_fashion_recommendation(style, occasion):
    recommendations = {
        ('casual', 'party'): "Try a fun, colorful dress or a cool graphic tee with jeans.",
        ('casual', 'work'): "Go for a smart casual look, like a blazer with jeans.",
        ('formal', 'party'): "Wear a sleek evening gown or a tuxedo for a classy look.",
        ('formal', 'work'): "A business suit or a professional dress would be perfect.",
        ('sportswear', 'outing'): "Comfortable activewear like leggings and a tank top.",
        ('sportswear', 'party'): "Casual but stylish sportswear can work for a laid-back party.",
    }
    return recommendations.get((style, occasion), "No recommendation available for this combination.")
click=st.button("Customize your wadrobe")
if click:
    genai.configure(api_key="AIzaSyAaA2z8clwJWN8Iwa-3O_WydZVAPyD2RgA")
    model=genai.GenerativeModel("gemini-1.5-flash")
    response=model.generate_content(f"clothing style{clothing_items},give me fashion recommendation{get_fashion_recommendation}")
    st.write(response.text)

