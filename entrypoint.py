import streamlit as st

# set page configurations for the whole app
st.set_page_config(page_title="handgemacht von svea", page_icon="🟠")

# sidebar layout
with st.sidebar:

    # place the image at the very top
    st.logo("images/svea_logo_transparent.png", size = "large")

    # add navigation below the image
    pg = st.navigation([
        st.Page("start_page.py"),
        st.Page("get_to_know_me.py"),
        st.Page("events.py"),
        st.Page("gallery.py"),
        st.Page("decision_help.py"),
        st.Page("randomizer.py"),
        st.Page("sign_up.py"),
        st.Page("craft_with_me.py"),
    ])

# run the navigation
pg.run()