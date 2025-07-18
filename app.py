import streamlit as st
import pandas as pd
from util import anime, anime_similarity, recommend_anime
from util import movie, movie_similarity, recommend_movies

st.title(f'Anime & Movies Recommendations')

st.sidebar.markdown("""
🛈 **Disclaimer:**
This recommendation engine has been trained on two datasets:
- **Anime:** ~12,000 entries  
- **Movies:** ~5,000 entries

As a result, recommendations may be more accurate for the Anime Dataset
""")

choice = st.radio(label=f"Select Recommendation Type: ", options=['Anime (TV/Movies)', 'Movie'])

name_input = st.text_input(f'Enter The {choice} Name: ')

top = st.slider(f'Number Of Recommendations', min_value=3, max_value=30, value=15)

if st.button("Recommend"):
    try:
        if choice == "Movie":
            data = recommend_movies(movie_name=name_input, movies_data=movie, similarity=movie_similarity, top_n=top+1)

        else:
            data = recommend_anime(title=name_input, df=anime, similarity=anime_similarity, top=top)

        st.success(f'Here Are Your Recommendations: ')
        st.dataframe(data)
    
    except Exception as e:
        st.error(f'Error: {e}')