import streamlit as st

# place header and divider
st.header("GALLERY", divider="orange")

# display the subtitle
st.markdown("*Browse through a collection of my favorite pieces*")

# display images unsing  column-layout
c1, c2, c3 = st.columns(3)
with c1:
    st.image("images/gallery/1_white.png")
with c2:
    st.image("images/gallery/2_white.png")
with c3:
    st.image("images/gallery/3_white.png")
with c1:
    st.image("images/gallery/4_orange.png")
with c2:
    st.image("images/gallery/5_orange.png")
with c3:
    st.image("images/gallery/6_red.png")
with c1:
    st.image("images/gallery/7_pink.png")
with c2:
    st.image("images/gallery/8_violet.png")
with c3:
    st.image("images/gallery/9_violet.png")
with c1:
    st.image("images/gallery/10_blue.png")
with c2:
    st.image("images/gallery/11_blue.png")
with c3:
    st.image("images/gallery/12_blue.png")
with c1:
    st.image("images/gallery/13_green.png")
with c2:
    st.image("images/gallery/14_green.png")
with c3:
    st.image("images/gallery/15_green.png")

# add information at the end of the page using html
st.markdown(
    "<br><hr><center><strong>Made with 🤍 by Svea</strong></a><br><br>Svea is the lovely founder of handgemacht von Svea :)</center><hr>",
    unsafe_allow_html=True)