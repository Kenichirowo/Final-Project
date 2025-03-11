import streamlit as st

# Set page configuration to wide mode for a larger container
st.set_page_config(layout="wide")

# Starting the app
st.title("Agenda & Project Overview")

# Embed Google Slides as a presentation using an iframe
embed_code = """
<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQzvDfO1HkUqewKCL10D59NXToLLFyIQdhJKrv0d0d3ZlqETOz4YLSqtsHhwkl_6Wro903UxI4wOQ60/embed?start=false&loop=false&delayms=60000" frameborder="0" width="1440" height="839" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
"""

# Display the Google Slides presentation in Streamlit
st.components.v1.html(embed_code, height=850, width=1455)
