import streamlit as st
import pandas as pd

# Reading the .csv files:
actors = pd.read_csv('../Data/Clean/actors_app.csv', sep=';')

# Set page configuration to wide mode for a larger container
st.set_page_config(layout="wide")

# Starting the app
st.title("Actors Dataset")

# Add a text input for searching by actor name
search_term = st.text_input("Search by Actor Name")

# Filter the DataFrame based on the search term
if search_term:
    filtered_actors = actors[actors['Name'].str.contains(search_term, case=False, na=False)]
else:
    filtered_actors = actors

# Display the filtered DataFrame
st.dataframe(data=filtered_actors, width=1350, height=500, use_container_width=False, hide_index=None, column_order=None, column_config=None, key=None, on_select="ignore", selection_mode="multi-row", row_height=None)

st.write("Actors with movie releases from 2010 onwards")