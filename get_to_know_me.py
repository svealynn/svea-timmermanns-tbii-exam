import streamlit as st

# place header and divider
st.header("GET TO KNOW ME", divider="orange")

# display the subtitle and add white space
st.markdown("*Learn more about the environmental benefits, creative processes, and my personal motivation behind upcycled jewelry*")
st.markdown(" ")

# use containers for horizontal layout
container1 = st.container(border=False)
container2 = st.container(border=False)
container3 = st.container(border=False)


# use columns for vertical layout
c1, c2 = container1.columns(2)

# place images of me
c1.image("images/me1.jpg", width=300)

# place subheader
c2.subheader ("About me")

# place text
c2.markdown("Hey! I'm Svea, and I’ve found my passion in upcycling old pearls into new, unique earrings. Explore my website to find the perfect earrings that match your style... or even get creative by yourself!")

# place divider
container2.markdown("___")

# place subheader
container3.subheader ("About upcycling")


# use columns fpr vertical layout
c1, c2 = container3.columns(2)

# place text
c1.markdown("In today's world, sustainability and environmental consciousness are crucial. Upcycled jewelry transforms discarded materials into unique accessories, reducing waste and minimizing our ecological footprint. The fashion industry is a major polluter, responsible for 10% of global carbon emissions. For example, mining for new metals and gemstones causes habitat destruction and water pollution. By choosing upcycled jewelry, we decrease the demand for new resources and help protect the environment.")

# place image on the right
c2.image("images/gallery/4_orange.png", width = 300)

# place image on the left
c1.image("images/gallery/6_red.png", width=300)

# place second part of the text
c2.markdown("Upcycled jewelry also supports ethical fashion by promoting a sustainable economy and eco-friendly practices. Each piece is a testament to creativity, combining elements of the past with modern design, resulting in one-of-a-kind creations. My passion for upcycled jewelry stems from a desire to make a positive impact. Transforming old pearls into new earrings allows me to contribute to sustainability while crafting beautiful, meaningful pieces. Together, we can make a difference, one unique piece at a time.")

# place divider
st.markdown ("___")

# place subheader
st.subheader ("Making of")

# display the subtitle
st.markdown("*Discover the process and craftsmanship that goes into each pair of earrings.*")

# place the video using a youtube reference
st.video("https://youtu.be/5nij1TnPrcE")


# add information at the end of the page using html
st.markdown(
    "<br><hr><center><strong>Made with 🤍 by Svea</strong></a><br><br>Svea is the lovely founder of handgemacht von Svea :)</center><hr>",
    unsafe_allow_html=True)