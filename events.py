import streamlit as st

# place header and divider
st.header("EVENTS", divider="orange")

# display the subtitle
st.markdown("*Meet me at the next market or participate at an upcoming jewerly making workshop :)*")

# show four events and give information
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.image("images/calendar/market.jpg", caption = "AStA-fleamarket at Leuphana University")
with c2:
    st.image("images/calendar/market_2.jpg", caption = "Taendelmarkt at museum Lüneburg")
with c3:
    st.image("images/calendar/workshop.jpg", caption = "jewelery making workshop at Digital Media study journey")
with c4:
    st.image("images/calendar/workshop_2.jpg", caption="jewelery making workshop with ROCK YOUR LIFE! Lüneburg")

# place divider
st.markdown("___")

# display a subheader
st.subheader("Calendar")

# display another subtitle for the calender-section
st.markdown("*Do you want to visit me at the next market or join a jewelery making event? Then have a look at my calendar and save the dates to your own calendar!*")

# embed calender
st.components.v1.iframe("https://calendar.google.com/calendar/embed?src=handgemacht.von.svea%40gmail.com&ctz=Europe%2FBerlin", height=400, scrolling=True)

# add information at the end of the page using html
st.markdown(
    "<br><hr><center><strong>Made with 🤍 by Svea</strong></a><br><br>Svea is the lovely founder of handgemacht von Svea :)</center><hr>",
    unsafe_allow_html=True)