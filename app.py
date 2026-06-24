import streamlit as st
import qrcode

st.set_page_config(
    page_title="QR-Code Generator",
    page_icon="🏷️")
st.title("QR-Code Generator")

text = st.text_input("What should be in the QR-Code?")

img = qrcode.make(text)
img.save("qr.png")


button = st.button("Generate")
if button:
   st.image("qr.png",width=300)






