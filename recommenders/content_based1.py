"""

    Content-based filtering for item recommendation.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: You are required to extend this baseline algorithm to enable more
    efficient and accurate computation of recommendations.

    !! You must not change the name and signature (arguments) of the
    prediction function, `content_model` !!

    You must however change its contents (i.e. add your own content-based
    filtering algorithm), as well as altering/adding any other functions
    as part of your improvement.

    ---------------------------------------------------------------------

    Description: Provided within this file is a baseline content-based
    filtering algorithm for rating predictions on Movie data.

"""

# Script dependencies
import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer
#from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer


# Streamlit dependencies
import streamlit as st
import joblib,os

# Importing data
movies = pd.read_csv('resources/data/movies.csv', sep = ',')
ratings = pd.read_csv('resources/data/ratings.csv')
movies.dropna(inplace=True)
#movies = pd.read_csv('resources/data/edsadata/movies.csv')
#imdb_data = pd.read_csv('resources/data/edsadata/imdb_data.csv')
#tags = pd.read_csv('resources/data/edsadata/tags.csv')
#train = pd.read_csv('resources/data/edsadata/train.csv')
#test = pd.read_csv('resources/data/edsadata/test.csv')

#df = imdb_data[['movieId','title_cast','director', 'plot_keywords']]
#df = df.merge(movies[['movieId', 'genres', 'title']], on='movieId', how='inner')
#ratings = train.merge(movies, on='movieId', how='inner')
#ratings.drop('timestamp', axis=1, inplace=True)

def data_preprocessing(data):
    """Prepare data for use within Content filtering algorithm.

    Parameters
    ----------
    subset_size : int
        Number of movies to use within the algorithm.

    Returns
    -------
    Pandas Dataframe
        Subset of movies selected for content-based filtering.

    """
    movies = data.copy()
    # Split genre data into individual words.
    #movies['keyWords'] = movies['genres'].str.replace('|', ' ')
    #movies['genres'] = movies['genres'].apply(str).apply(lambda x: x.split('|'))
    # Subset of the data
    #movies_subset = movies[:subset_size]
    # Separate genre using a ',' instead of '|'.
    movies['bag_of_words'] = movies['genres'].str.replace('|', ' ')

    movies['genres'] = movies['genres'].apply(str).apply(lambda x: x.split('|'))
    return movies

   

# !! DO NOT CHANGE THIS FUNCTION SIGNATURE !!
# You are, however, encouraged to change its content.  
def content_model(movie_list,top_n=10):
    """Performs Content filtering based upon a list of movies supplied
       by the app user.

    Parameters
    ----------
    movie_list : list (str)
        Favorite movies chosen by the app user.
    top_n : type
        Number of top recommendations to return to the user.

    Returns
    -------
    list (str)
        Titles of the top-n movie recommendations to the user.

    """
    # Initializing the empty list of recommended movies
    movies_df = data_preprocessing(movies)
    genre_list = []
    for i in movie_list:
        genre_list.append(list(movies_df[movies_df['title'] == i]['genres'])[0])

    # instantiate the multilabelbinarizer for sparsity
    mlb = MultiLabelBinarizer()
    mlb.fit_transform(genre_list)
    genre_list = mlb.classes_
    movies_df = movies_df[~movies_df['title'].isin(movie_list)]  # remove selected movies
    movie_genre = movies_df

    # looping over genres for similarity
    for i in genre_list:

        movie_genre = movie_genre[movie_genre['bag_of_words'].str.contains(i)]

        if len(movie_genre) <= top_n:
            break

        movie_genre_2 = movie_genre

    movie_rating = ratings[ratings['movieId'].isin(movie_genre_2['movieId'].values)][['movieId', 'rating']]

    top_movies = (movie_rating.groupby(['movieId']).mean().reset_index()).sort_values('rating', ascending=False)[:top_n]

    return list((movies_df[movies_df['movieId'].isin(top_movies['movieId'].values)]['title']).values)
   
