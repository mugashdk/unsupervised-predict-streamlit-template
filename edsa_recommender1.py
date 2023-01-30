"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Solution Overview","About Us"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")

        st.image('resources/imgs/logo1.jpg',use_column_width=True)
    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------


    if page_selection == "Solution Overview":
        #st.title("Solution Overview")
        #st.title("My Title", style={"color": "green"})
    
        st.markdown("<h1 style='color: #67B69B;'>Solution Overview</h1>", unsafe_allow_html=True)
        st.image('resources/imgs/logo1.jpg',use_column_width=True)


        st.write("<h2 style='color: #37199A;'>Introduction</h2>", unsafe_allow_html=True)
        st.markdown("In the modern world, Recommender Systems play a crucial role in driving social and \
		economic success by providing individuals with relevant content that aligns with their             \
		interests. Our company offers a cutting-edge solution to enhance the movie-watching experience.           \
		")
        
        st.markdown("Our algorithm accurately predicts User's rating of a movie they have not viewed based on their historical preferences.    \
        Our recommendation engine has the potential to revolutionize the film industry, \
        similar to how tech giants such as Amazon, YouTube, and Facebook have utilized  \
        recommender systems to improve their user experience. Companies like Netflix and \
        Spotify have already proven the profitability of a successful recommendation engine, \
        and we aim to bring that success to the film industry.\
        Invest in the future of the film industry and join us in revolutionizing the movie-watching experience.") 

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
    if page_selection == "About Us":
        st.markdown("<h1 style='color: #67B69B;'>About Us</h1>", unsafe_allow_html=True)
        # You can read a markdown file from supporting resources folder

        st.write("<h2 style='color: #37199A;'>The Company</h2>", unsafe_allow_html=True)
        st.markdown(" Dataverse is a ...")

        st.subheader("Meet the Team ")
        if st.button('Farayi'): # information is hidden if button is clicked
            st.markdown('Farayi Myambo is a the Dataverse CEO')
        if st.button('David'): # information is hidden if button is clicked
            st.markdown('David Mugambi is a Dataverse Project Manager')
        if st.button('Chinonso'): # information is hidden if button is clicked
            st.markdown('Chinonso Agulonu is a Dataverse Developer/Strategist')
        if st.button('Josiah'): # information is hidden if button is clicked
            st.markdown('Joy Obukohwo is a Dataverse Developer/strategist')
        if st.button('Orismeke'): # information is hidden if button is clicked
            st.markdown('Orisemeke ibude is the Dataverse Product lead')
        if st.button('Temitope'): # information is hidden if button is clicked
            st.markdown('Temitope Olaitan is the Dataverse Communictions')

        st.image('resources/imgs/logo1.jpg',use_column_width=True)



if __name__ == '__main__':
    main()

