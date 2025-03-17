import pandas as pd
import streamlit as st
import warnings
import random
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

playlist = pd.read_csv('Musique/BD/films_a_jour.csv', index_col=0)

voir = st.checkbox('Voir ma liste de films.')

if voir:
    st.dataframe(playlist)


# PROPOSITION ARTISTE

st.header('Choix film')

choix_genre = st.toggle('Je veux un genre précis.', value = False)

if choix_genre:

    genre = st.selectbox('Choisissez le genre:', list(playlist['Genre'].unique()))
    playlist = playlist[playlist['Genre'] == genre]

proposition = st.checkbox('Propose moi un film')

if proposition:
    liste_artistes = list(playlist['titre'].unique())
    artiste_aleatoire = random.choice(liste_artistes)
    st.markdown(artiste_aleatoire)

    acceptation = st.checkbox('OK je vais regarder ça.')
    
    if acceptation:
        playlist = playlist[playlist['Titre'] != artiste_aleatoire]
        playlist.to_csv('Musique/BD/films_a_jour.csv')
        playlist = pd.read_csv('Musique/BD/films_a_jour.csv', index_col=0)
