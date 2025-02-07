import streamlit as st
import random
from helpers import generate_response, get_images

# place header and divider
st.header("CRAFT WITH ME", divider="orange")

# Display the subtitle
st.markdown("*Are you inspired? Now it is your turn! Get cozy and start your upcycling jewelry journey with me :)*")

#create tabs for navigation
tabs1, tabs2, tabs3 = st.tabs(["Pinterest-Board", "Image Search", "Get Help"])

# use tab1 for pinterest board
with tabs1:

    # place subheader
    tabs1.subheader("Pinterest-Board")

    # Display the subtitle
    st.markdown("*Have a look at my pinterest board for inspiration*")

    # add button that leads to pinterest, sadly pinterest would not let me embed the page
    st.image("images/pinterest.png")

    # use columns layout to place buttons next to another
    c1,c2 = st.columns(2)
    with c1:
        # button that leads to my personal pinterest board
        st.link_button("Open Sveas pinterest-board", "https://de.pinterest.com/nnylaevs/schmuck/", use_container_width=True)
    with c2:
        # button that leads to the pinterest homepage
        st.link_button("Open pinterest start page", "https://de.pinterest.com/", use_container_width=True)

# use tab2 for api image search
with tabs2:

    # place subheader
    tabs2.subheader("Image Search")

    # Display the subtitle
    st.markdown("*Search for inspirational images. Try it with summer holiday or fashion show!*")

    # display banner image
    st.image("images/banners/image_search_banner.png")

    # Th following code is cde from class adjusted to my app
    api_key = st.secrets['unsplash_api_key']

    # Get researched image
    # create a text box in streamlit
    search_word = st.chat_input(
        "Enter image search here")

    # show three images
    if search_word:
        try:
            images = get_images(search_word, api_key)
            image_1 = random.choice(images)
            image_2 = random.choice(images)
            image_3 = random.choice(images)

            # use columns to place results next to another
            c1, c2, c3 = st.columns(3)
            c1.image(image_1, caption=f"Your first {search_word} image")
            c2.image(image_2, caption=f"Your second {search_word} image")
            c3.image(image_3, caption=f"Your third {search_word} image")

        # place warning for user feedback if something is not working
        except:
            st.warning("Sorry, I can't offer you something fitting to your search :( Try another search")

# use tabs 3 for a help section including a faq
with tabs3:

    # place subheader
    tabs3.subheader("Get Help from Lynn")

    # display the subtitle
    st.markdown("*Get help from your diy-assistant Lynn with your questions regarding the crafting process*")

    # use columns to place content next to another
    c1, c2 = st.columns(2)
    with c1:
        # display image of chatbot
        st.image("images/chatbot.jpg", caption="Lynn image created by copilot")
    with c2:
        # headline for better usability
        st.markdown("**FAQ**")
        # use expanders to show and hide answers
        expander = st.expander("What wire should I use?")
        expander.write('''
                    I recommend aluminium wire. It is easy to bend by hand and does not loose its color by time.
                ''')
        expander = st.expander("What tools should I use?")
        expander.write('''
                    I personally use three tools: One pair of pliers for cutting the wire, one pair of pliers for bending the wire and one pair of pliers for forming nice and round circles.
                ''')
        expander = st.expander("Why does my wire not look shiny and sleek?")
        expander.write('''
                    Make sure to not bend the wire unnecessary often. Also make sure to not push the wire to hard with your pliers.
                ''')
        expander = st.expander("Where can I find good pearls?")
        expander.write('''
                    Try to look for your pearls in second hand shops or ask your friends ans family for old jewelery they do not need anymore.
                ''')
        expander = st.expander("Do I need experience in jewerly making?")
        expander.write('''
                    No! You can start with easy designs and will get better from time to time. ut even easy designs look qualitative and chic!
                ''')



    # user message
    prompt = st.chat_input("Enter an individual question")

    if prompt:
        with st.chat_message("assistant"):
            # add info, user feedback in case hugchat does not work
            with st.spinner("Thinking... Please note, that my system might be overrunning and I can't guarantee an answer"):
                response = generate_response(prompt)

                # user friendly presentation of the response
                st.markdown(response)

# click to play chill music
st.markdown("---")
st.markdown("*Play some chill music if you wish*")
st.audio("music/chill_music.mp3", format="audio/mpeg", loop=True)

# add information at the end of the page using html
st.markdown(
    "<br><hr><center><strong>Made with 🤍 by Svea</strong></a><br><br>Svea is the lovely founder of handgemacht von Svea :)</center><hr>",
    unsafe_allow_html=True)