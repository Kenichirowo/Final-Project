import streamlit as st
import pandas as pd

## Reading the .csv files:
actors = pd.read_csv('../Data/Clean/actors_app.csv', sep=';')
movies = pd.read_csv('../Data/Clean/movies_app.csv', sep=';')

# Set page configuration to wide mode for a larger container
st.set_page_config(layout="wide")

# Starting the app
st.title("Movies Database")

st.dataframe(movies)

st.dataframe(data=movies, width=1000, height=None, use_container_width=False, hide_index=None, column_order=None, column_config=None, key=None, on_select="ignore", selection_mode="multi-row", row_height=None)