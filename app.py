import pandas as pd
import streamlit as st
import pickle
import requests
# response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=b41689f7cacd82c99447fbf9532d426e&language=en-US'.format(161))
# data=response.json()
# print(data['belongs_to_collection']['poster_path'])
# full_path="https://image.tmdb.org/t/p/w500/"+data['belongs_to_collection']['poster_path']
# print(full_path)
def fetch_posters(movie_id):

    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=b41689f7cacd82c99447fbf9532d426e&language=en-US'.format(movie_id))
    data=response.json()
    # print(data['belongs_to_collection']['poster_path'])
    # poster_path=data['poster_path']
    # full_path="https://image.tmdb.org/t/p/w500/"+data['belongs_to_collection']['poster_path']
    return "https://image.tmdb.org/t/p/w500/"+data['belongs_to_collection']['poster_path']


def recommend(movie):

    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    # recommended_movie_posters = []
    for i in movie_list:
        movie_id=i[0]

        recommended_movies.append(movies.iloc[i[0]].title)
        # recommended_movie_posters.append(fetch_posters(movie_id))
    return recommended_movies
    # return recommended_movies, recommended_movie_posters


st.title("Movie Recommender System")

movies_list=pickle.load(open("movies_dict.pkl", "rb"))
movies=pd.DataFrame(movies_list)
similarity=pickle.load(open("similarity.pkl", "rb"))
selected_movie=st.selectbox(
    '',
    movies['title'].values
)


if st.button('Recommend similar'):
    # names=recommend(selected_movie)
    recommendations=recommend(selected_movie)
    for i in recommendations:
        st.write(i)

#
#     col1, col2, col3, col4, col5=st.beta_columns(5)
#     with col1:
#         st.header()
#         st.image()
#     with col2:
#         st.header()
#         st.image()
#     with col3:
#         st.header()
#         st.image()
#     with col4:
#         st.header()
#         st.image()
#     with col5:
#         st.header()
#         st.image()
