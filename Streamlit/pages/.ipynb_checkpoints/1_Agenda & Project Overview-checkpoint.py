import streamlit as st

# Set page configuration to wide mode for a larger container
st.set_page_config(layout="wide")

# Starting the app
st.title("Embed Google Slides Presentation in Streamlit")

# Embed Google Slides as a presentation using an iframe
embed_code = """
<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vTgcGbf1TVH7LFUCt8IqNX_NOgww0Y_kpmfVt2avIkB02hMR5t8ZZvYtXrraL1Z4b0moWyP8yRAqKht/embed?start=false&loop=false&delayms=3000" frameborder="0" width="1440" height="839" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
"""

# Display the Google Slides presentation in Streamlit
st.components.v1.html(embed_code, height=850, width=1455)

st.write("This is an example of how to embed Google Slides as a presentation in a Streamlit app.")
