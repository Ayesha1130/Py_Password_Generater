import streamlit as st
import random
import string

def password_generaters(Lenght, use_digit, use_special):
    characters = string.ascii_letters

    if use_digit:
        characters += string.digits

    if use_special:
        characters += string.punctuation

    return ''.join(random.choice(characters)for _ in range(Lenght))

st.title('Password Generater')

Lenght = st.slider('Password Lenght', min_value=10, max_value=30, value=14)


use_digit = st.checkbox('Include Digits')

use_special = st.checkbox('Use Special Charaters')

if st.button('Generate Password'):
    password = password_generaters(Lenght, use_digit, use_special)
    st.success(f'Your Password: {password}')
    st.balloons()
   
    st.info('This password generator uses the secrets module in Python, which is a high-level cryptography library. It is not suitable for generating passwords for sensitive applications.')
st.write('---------------------------------------')
st.write('Build with ❤️ by [Ayesha Iqbal](https://www.linkedin.com/in/ayesha-iqbal-2613402b4/)')

