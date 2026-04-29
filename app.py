import streamlit as st
import pickle as pkl
import pandas
import requests


st.title("Movie Recommendation System")

# Load data
new_df=pkl.load(open("movies.pkl","rb"))
similarity=pkl.load(open("similarities.pkl","rb"))
movies_list=new_df['title'].values

# TMDB API Configuration
TMDB_API_KEY = "e767d1397d022156ec4e7c366870bea2"  # Replace with your TMDB API key

def fetch_poster(movie_id):
    """Fetch movie poster from TMDB API"""
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
        response = requests.get(url)
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
        return None
    except:
        return None

def recommendation(movie):
    """Get movie recommendations with posters"""
    movie_index=new_df[new_df['title']==movie].index[0]
    distances=similarity[movie_index]
    all_recos=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies=[]
    recommended_posters=[]

    for i in all_recos:
        movie_id = new_df.iloc[i[0]].movie_id
        recommended_movies.append(new_df.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters

selected_movie_name=st.selectbox("Select a movie you like:",(movies_list))

if st.button("Recommend"):
    recommendations, posters = recommendation(selected_movie_name)

    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.text(recommendations[idx])
            if posters[idx]:
                st.image(posters[idx])
            else:
                st.write("No poster available")



