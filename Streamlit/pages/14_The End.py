import streamlit as st

# Set page configuration to wide mode for a larger container
st.set_page_config(layout="wide")

# The end image
st.image("img/theend.jpg", width=1000)

st.write("")
st.write("")

# Create columns for layout
col1, col2, col3 = st.columns([1, 2, 1])  # Adjust the ratio to fit your design

# first column
with col1:
    st.image("img/ironhack.png", width=100)

# second column
with col2:
    st.header("By Víctor Ramírez Rubio")

# third column
with col3:
    if st.button("Thank you!"):
        st.audio("sound/indy_motif.mp3", , autoplay=True) # Trigger the audio
        st.balloons()
