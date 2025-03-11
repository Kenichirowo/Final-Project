import streamlit as st
import pandas as pd

# Reading the .csv files
movies = pd.read_csv('../Data/Clean/movies_app.csv', sep=';')

# Set page configuration for a wide layout
st.set_page_config(layout="wide")

# Starting the app
st.title("Movies Dataset")

# Ensure column names are clean and manage genre filtering
movies.columns = movies.columns.str.strip()

# Multiselect widget for genre choice
if 'Movie_Genre' in movies.columns:
    genre_options = movies['Movie_Genre'].unique()
    selected_genres = st.multiselect('Select movie genres to filter by:', genre_options, default=genre_options)

    # Filter movies based on selected genres
    filtered_movies = movies[movies['Movie_Genre'].isin(selected_genres)]
else:
    st.error('Column "Movie_Genre" not found.')
    filtered_movies = movies

# Add a slider for filtering by Average_Rating (ensure correct column name)
if 'Average_Rating' in filtered_movies.columns:
    min_rating = float(filtered_movies['Average_Rating'].min())
    max_rating = float(filtered_movies['Average_Rating'].max())

    selected_rating = st.slider('Select rating range:', min_value=min_rating, max_value=max_rating, value=(min_rating, max_rating), step=0.1)

    # Filter movies based on selected rating range
    filtered_movies = filtered_movies[filtered_movies['Average_Rating'].between(*selected_rating)]
else:
    st.error('Column "Average_Rating" not found.')

# Display the filtered DataFrame
st.dataframe(data=filtered_movies, width=1350, height=500, use_container_width=False)

st.write("Movie releases from 2010 onwards")
