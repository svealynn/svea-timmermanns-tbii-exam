import streamlit as st

# place header and divider
st.header("WELCOME!", divider="orange")

# add white space
st.write(" ")
st.write(" ")

c1, c2 = st.columns(2)
with c1:
    # add white space
    st.write(" ")
    st.subheader("Hi there!")
    st.markdown("I am more than happy to welcome you on my app! I am Svea, and I’ve found my passion in upcycling earrings. With this page I want to share my lovely hobby. This page is promoting my own earrings and events as well as it helps you with your own upcycling jewelery journey!")
    st.markdown("Lots of Love, Svea")

with c2:
    # place images
    st.image("images/me.jpg", width=250)

# place divider
st.markdown("___")

# add subheader for better usability
st.subheader("Tutorial")

# add expander to show the tutorial
expander = st.expander("Click here to see the tutorial")

with expander:

    # place subheader
    st.subheader("How to use the app")

    # use container for horizontal layout
    container1 = st.container(border=False)
    container2 = st.container(border=False)
    container3 = st.container(border=False)

    # use columns for vertical layout
    c1, c2, c3 = container1.columns(3)
    with c1:
        # display image
        st.image("images/start_page/get_to_know_me.png")
        # display description
        st.markdown("**Get to know me**, the art of uypcycling and find out about my process of upcycling in a cozy video.")
    with c2:
        # display image
        st.image("images/start_page/events.png")
        # display description
        st.markdown("Learn more about the **events** I participate in and visit me at the next one. Look at my calendar to see the dates")
    with c3:
        # display image
        st.image("images/start_page/gallery.png")
        # display description
        st.markdown("Look through my **gallery** to get inspired or decide which ones to buy at the next market.")

    c1, c2, c3 = container2.columns(3)
    with c1:
        # display image
        st.image("images/start_page/decision_help.png")
        # display description
        st.markdown("Play through a **decision help** to get to know the perfect earrings for your style")
    with c2:
        # display image
        st.image("images/start_page/randomizer.png")
        # display description
        st.markdown("... or let the **randomizer** decide your fate!")
    with c3:
        # display image
        st.image("images/start_page/sign_up.png")
        # display description
        st.markdown("If you want to support me and my hobby, make shure to **sign up** for my newsletter.")

    # display image
    container3.image("images/start_page/craft_with_me.png")
    # display description
    container3.markdown("**Craft with me** and get started on your own! Start the cozy music, look for inspiration on pinterest, use my images search for more neutral inspiration. Any questions? Look at the help tab to get help from my diy-assistant Lynn :)")

# add information at the end of the page using html
st.markdown(
    "<br><hr><center><strong>Made with 🤍 by Svea</strong></a><br><br>Svea is the lovely founder of handgemacht von Svea :)</center><hr>",
    unsafe_allow_html=True)