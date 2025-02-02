import streamlit as st

# place header and divider
st.header("DECISION HELP", divider="orange")

# display the subtitle
st.markdown(
    "*Need assistance choosing the right pair? Get personalized recommendations. (Either to buy at the market or to do it yourself)*"
)

# display questions on the left, result on the right
c1, c2 = st.columns(2)

with c1:

    # user input using radio buttons
    length = st.radio(
        "**1 I Do you prefer long or short earrings?**",
        ["long", "short"],
        index=None,
    )

    colour = st.radio(
        "**2 I Do you like to wear colours or plain tones?**",
        ["colours", "plain tones"],  # Corrected "plains" to "plain tones"
        index=None,
    )

    silver_gold = st.radio(
        "**3 I Are you a silver or a gold person?**",
        ["silver", "gold"],
        index=None,
    )

    style = st.radio(
        "**4 I Do you like to dress chic or experimental?**",
        ["chic", "experimental"],
        index=None,
    )

# define start image
decision_help_result = "images/decision_help/white.png"

# decision logic
if length == "long" and colour == "colours" and silver_gold == "silver" and style == "chic":
    decision_help_result = "images/decision_help/1_earring.jpg"
elif length == "long" and colour == "colours" and silver_gold == "silver" and style == "experimental":
    decision_help_result = "images/decision_help/2_earring.jpg"
elif length == "long" and colour == "colours" and silver_gold == "gold" and style == "chic":
    decision_help_result = "images/decision_help/3_earring.jpg"
elif length == "long" and colour == "colours" and silver_gold == "gold" and style == "experimental":
    decision_help_result = "images/decision_help/4_earring.jpg"
elif length == "long" and colour == "plain tones" and silver_gold == "silver" and style == "chic":
    decision_help_result = "images/decision_help/5_earring.jpg"
elif length == "long" and colour == "plain tones" and silver_gold == "silver" and style == "experimental":
    decision_help_result = "images/decision_help/6_earring.jpg"
elif length == "long" and colour == "plain tones" and silver_gold == "gold" and style == "chic":
    decision_help_result = "images/decision_help/7_earring.jpg"
elif length == "long" and colour == "plain tones" and silver_gold == "gold" and style == "experimental":
    decision_help_result = "images/decision_help/8_earring.jpg"
elif length == "short" and colour == "colours" and silver_gold == "silver" and style == "chic":
    decision_help_result = "images/decision_help/9_earring.jpg"
elif length == "short" and colour == "colours" and silver_gold == "silver" and style == "experimental":
    decision_help_result = "images/decision_help/10_earring.jpg"
elif length == "short" and colour == "colours" and silver_gold == "gold" and style == "chic":
    decision_help_result = "images/decision_help/11_earring.jpg"
elif length == "short" and colour == "colours" and silver_gold == "gold" and style == "experimental":
    decision_help_result = "images/decision_help/12_earring.jpg"
elif length == "short" and colour == "plain tones" and silver_gold == "silver" and style == "chic":
    decision_help_result = "images/decision_help/13_earring.jpg"
elif length == "short" and colour == "plain tones" and silver_gold == "silver" and style == "experimental":
    decision_help_result = "images/decision_help/14_earring.jpg"
elif length == "short" and colour == "plain tones" and silver_gold == "gold" and style == "chic":
    decision_help_result = "images/decision_help/15_earring.jpg"
elif length == "short" and colour == "plain tones" and silver_gold == "gold" and style == "experimental":
    decision_help_result = "images/decision_help/16_earring.jpg"
else:
    decision_help_result = "images/decision_help/white.png"

# user instructions
with c2:
    st.markdown("*Answer the questions to discover your perfect match. Change your answers if you wish*")
    # images is being shown and updated with every change
    st.image(decision_help_result, caption = "My recommendation for you")

# add information at the end of the page using html
st.markdown(
    "<br><hr><center><strong>Made with 🤍 by Svea</strong></a><br><br>Svea is the lovely founder of handgemacht von Svea :)</center><hr>",
    unsafe_allow_html=True)
