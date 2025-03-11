import streamlit as st
import pandas as pd

# Set page configuration to wide mode for a larger container
st.set_page_config(layout="wide")

# Starting the app
st.image("img/Movies_app.png", width=1000)

# Create columns for layout
col1, col2 = st.columns([1, 13])  # Adjust the ratio to fit your design

# Display the image in the first column
with col1:
    st.image("img/ironhack.png", width=100)

# Display the title in the second column
with col2:
    st.title("Data Analytics Final Project")
    
st.header("By Víctor Ramírez Rubio")

st.write("")
st.write("")
st.write("")
st.write("")
st.markdown(
    """
    ### Features of the App
    - **Project Presentation**:  Explanation of key project points.
    - **Data Visualization**: Interactive charts and graphs.
    - **User Interaction**: Buttons, sliders, and input fields.
    - **Data Analysis**: Real-time data processing and analysis.
    - **Customization**: Easy to customize and extend.
    """
)