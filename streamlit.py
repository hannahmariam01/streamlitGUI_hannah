import streamlit as st

st.set_page_config(page_title="Welcome", page_icon="👋", layout="centered")

st.markdown("<h1 style='text-align: center; color: white;'>👋 Welcome to My Streamlit App!</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>We're glad you're here. Let's explore together!</p>", unsafe_allow_html=True)

st.image(r"C:\Users\Hannah\OneDrive\Desktop\Python (sem 5)\my_photo.jpg", caption="That's me!", width=200)
