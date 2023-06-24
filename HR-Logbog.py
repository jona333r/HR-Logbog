import streamlit as st
from fpdf import FPDF
import base64
import webbrowser

col1, col2, col3, col4 = st.columns(4)

url = 'http://192.168.10.126:8502'


with col4:
    if st.button('Download som PDF?'):
        webbrowser.open_new_tab(url)

st.header(":mailbox: HR Logbog  (Mail)")


contact_form ="""
<form action="https://formsubmit.co/jona333r@edu.sde.dk" method="POST">
     <input type="text" name="Navn" placeholder="Navn" required>
     <input type="email" name="Email" placeholder="E-Mail" required>
     <input type="adresse" name="Adresse" placeholder="Adresse">
     <input type="number" name="Telefon" placeholder="Telefon nummer">
     <input type="stilling" name="Stilling" placeholder="Job-stilling" required>
     <textarea name="Kommentarer" placeholder="Tilføj en kommentar"></textarea>
     <button type="submit">Send</button>
     <input type="hidden" name="_next" value="http://192.168.10.126:8501">
     <input type="hidden" name="_blacklist" value="spammy pattern, banned term, phrase">
</form>
"""




def style_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown(contact_form, unsafe_allow_html=True)

style_css("style.css")

