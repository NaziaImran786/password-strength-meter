import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits #add numbers (0,9) if selected

    if use_special:
        characters += string.punctuation # Add special charactors (!, @, $, %, ^, &, *)

    return ''.join(random.choice(characters) for _ in range(length))

st.title("Password Generator")

st.markdown("""
    <style>
    .main {
        background-color: #FF7CFD,
    }
    .stButton>button {
        background-color: #ffffff
        color: black
    }
    .stTextInput>div>div>input {
        background-color: black;
        color: white;
    }            
    </style>
    """, unsafe_allow_html=True)

length = st.slider("Select password length", min_value=6, max_value=32, value=12)

use_digits = st.checkbox("Include Digits")

use_special = st.checkbox("Include special charactors")

if st.button("generate password"):
    password = generate_password(length, use_digits, use_special)
    st.write(f"Generate Password : {password}")

    st.success(f"Generated Password: {password}")

    st.write("_____________________________")

    st.write("Made by Nazia Imran")