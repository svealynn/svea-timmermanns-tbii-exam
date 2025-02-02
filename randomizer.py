import streamlit as st
import random

# place header and divider
st.header("RANDOMIZER", divider="orange")

# define earring options
options = [
    "images/decision_help/1_earring.jpg",
    "images/decision_help/2_earring.jpg",
    "images/decision_help/3_earring.jpg",
    "images/decision_help/4_earring.jpg",
    "images/decision_help/5_earring.jpg",
    "images/decision_help/6_earring.jpg",
    "images/decision_help/7_earring.jpg",
    "images/decision_help/8_earring.jpg",
    "images/decision_help/9_earring.jpg",
    "images/decision_help/10_earring.jpg",
    "images/decision_help/11_earring.jpg",
    "images/decision_help/12_earring.jpg",
    "images/decision_help/13_earring.jpg",
    "images/decision_help/14_earring.jpg",
    "images/decision_help/15_earring.jpg",
    "images/decision_help/16_earring.jpg"
]

# definition for randomizing earrings
def random_earrings():
    random_earrings_selection = random.choice(options)
    return random_earrings_selection

# define start image
random_earrings_selection = "images/decision_help/white.png"

# display the subtitle
st.markdown("*Feeling adventurous? Let the randomizer suggest a unique pair just for you. (Either to buy at the market or to do it yourself)*")

c1, c2 = st.columns(2)

with c1:
    # create a placeholder to update the image
    image_placeholder = st.empty()

    # display the selected image (or initial image)
    image_placeholder.image(random_earrings_selection, width = 340)

    # place randomize button
    randomize_button = st.button("randomize", use_container_width=True)

    if randomize_button:
        # update the image by selecting a random earring image
        random_earrings_selection = random_earrings()
        # update the image in the placeholder
        image_placeholder.image(random_earrings_selection, width = 340)



# add information at the end of the page using html
st.markdown(
    "<br><hr><center><strong>Made with 🤍 by Svea</strong></a><br><br>Svea is the lovely founder of handgemacht von Svea :)</center><hr>",
    unsafe_allow_html=True)
