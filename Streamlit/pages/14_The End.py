import streamlit as st

# Set page configuration to wide mode for a larger container
st.set_page_config(layout="wide")

# Starting the app
st.image("img/theend.jpg", width=1000)

st.write("")
st.write("")


# Create columns for layout
col1, col2, col3 = st.columns([1, 2, 1])  # Adjust the ratio to fit your design

# Display the header in the first column
with col1:
    st.image("img/ironhack.png", width=100)

# Display the button and balloons in the second column
with col2:
    st.header("By Víctor Ramírez Rubio")

# Display the image in the third column
with col3:
    if st.button("Thank you!"):
        st.balloons()
