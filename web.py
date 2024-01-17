import streamlit as st
from googletrans import Translator

p = Translator()

def french(text):
    translated = p.translate(text, dest='french')
    return translated

def german(text):
    translated = p.translate(text, dest='german')
    return translated

def yoruba(text):
    translated = p.translate(text, dest='yo')
    return translated

def Korean(text):
    translated = p.translate(text, dest='korean')
    return translated
def chinese(text):
    translated = p.translate(text, dest='zh-tw')
    return translated

st.title('Language Translation App')
text = st.text_area("Enter text here:", "")

option = st.selectbox(
                             'Select a Language:',
                              ['French', 'German', 'Yoruba', 'Korean', 'Chinese'], index=0)
st.write('You selected:', option)

mode = 1

if option=='French':
    mode = 1
if option == 'German':
    mode = 2
if option == 'Yoruba':
    mode = 3
if option == 'Korean':
    mode = 4
if option == 'Chinese':
    mode = 5

if mode==1:
     if st.button('Translate'):
        output = french(text)
        output_str = output
        translated_text = output_str.text
        st.success(translated_text)

if mode==2:
     if st.button('Translate'):
        output = german(text)
        output_str = output
        translated_text = output_str.text
        st.success(translated_text)
if mode==3:
     if st.button('Translate'):
        output = yoruba(text)
        output_str = output
        translated_text = output_str.text
        st.success(translated_text)
if mode==4:
     if st.button('Translate'):
        output = Korean(text)
        output_str = output
        translated_text = output_str.text
        st.success(translated_text)
if mode==5:
    if st.button('Translate'):
        output = chinese(text)
        output_str = output
        translated_text = output_str.text
        st.success(translated_text)