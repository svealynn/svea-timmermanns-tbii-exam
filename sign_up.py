import streamlit as st
from helpers import connect_to_mongo

# place header and divider
st.header("SIGN UP", divider="orange")

# display the subtitle
st.markdown("*Do you wish to hear about news in my newsletter? Don't waste any time and sign up now :)*")

# add white space
st.write(" ")

# create a text box for input
enter_address = st.text_input("Enter your e-mail-address to sign up for my newsletter")

if enter_address:
    try:
        # write data in database, so I can look at the database to use the e-mail-addresses for my newsletter
        db_name = "handgemacht_von_svea"
        collection_name = "newsletter"
        client = connect_to_mongo()
        db = client[db_name]
        collection = db[collection_name]

        # create a document
        document = {
            "e-mail": enter_address
        }

        # insert into mongoDB
        collection.insert_one(document)

        # give user feedback
        st.write(" ")
        st.markdown(f"Thank you for signing up with ***{enter_address}*** <3")

    # give user feedback of something is not working
    except:
        st.warning("Sorry, that did not work")

# add information at the end of the page using html
st.markdown(
    "<br><hr><center><strong>Made with 🤍 by Svea</strong></a><br><br>Svea is the lovely founder of handgemacht von Svea :)</center><hr>",
    unsafe_allow_html=True)
