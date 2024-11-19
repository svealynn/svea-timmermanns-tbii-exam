import streamlit as st
from decode_qrcode_page import decode_qrcode_page
from generate_qrcode_page import generate_qrcode_page


st.set_page_config(
    page_title="QR Code Generator v2",
    page_icon="💫"
)

# create a side bar with different pages
options = ['Generate QR Code', 'Decode QR Code', 'About Me']
page_selection = st.sidebar.selectbox("Menu", options)

# when the user selects a page, we want to show something
if page_selection == "Generate QR Code":
    generate_qrcode_page()
elif page_selection == "Decode QR Code":
    decode_qrcode_page()
elif page_selection == "About Me":
    st.write("HI! My Name is Svea ❤️")
    st.image("me.png",
             caption="MEEEE")
