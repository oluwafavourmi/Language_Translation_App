import streamlit as st
from googletrans import Translator

p = Translator()

def translate(text):
    translated = p.translate(text, dest='french')
    return translated

st.title('Language Translation App')
text = st.text_input('Enter your text here')

if st.button('Translate'):
   output = translate(text)
   st.success(output)

