import pandas as pd
import streamlit as st
import warnings
import random
import numpy as np

warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

# Chargement des fichiers CSV
playlist_film = pd.read_csv('https://docs.google.com/spreadsheets/d/1Uw59rRaTDXjfiMNiGco1FZO4VI5wkIer0bxllLiHxVQ/export?format=csv&gid=442082949#gid=442082949')
playlist_film_selection = playlist_film.copy()
playlist_film_selection2 = playlist_film.copy()
playlist_musique = pd.read_csv('https://docs.google.com/spreadsheets/d/1Uw59rRaTDXjfiMNiGco1FZO4VI5wkIer0bxllLiHxVQ/export?format=csv&gid=0#gid=0')
playlist_musique_selection = playlist_musique.copy()
playlist_livre = pd.read_csv('https://docs.google.com/spreadsheets/d/1Uw59rRaTDXjfiMNiGco1FZO4VI5wkIer0bxllLiHxVQ/export?format=csv&gid=1652576992#gid=1652576992')
playlist_livre_selection = playlist_livre.copy()

st.header('Puisse le sort vous être favorable.')

st.markdown("<hr style='border: 1px solid white; width: 100%;'>", unsafe_allow_html=True)

actions = ['Je veux ...', 'Un Film', 'Une Musique', 'Un Livre']

action = st.selectbox('Que souhaitez-vous faire ?', actions)


if action == 'Une Musique':
    col1, col2, col3 = st.columns(3)

    with col1:
        choix_genre = st.toggle('Je veux un style de musique précis.', value=False)
        if choix_genre:
            liste_genres = list(playlist_musique['Genre'].unique())
            liste_genres = [genre for genre in liste_genres if pd.notna(genre)]
            liste_genres.sort()

            genre = st.selectbox('Choisissez le genre:', liste_genres)
            playlist_musique_selection = playlist_musique_selection[playlist_musique_selection['Genre'] == genre]

    with col2:
        choix_francais = st.toggle('Je veux de la musique française.', value=False)
        if choix_francais == True:
            playlist_musique_selection = playlist_musique_selection[playlist_musique_selection['Français'] == True]
        else:
            playlist_musique_selection = playlist_musique_selection[playlist_musique_selection['Français'] == False]

    with col3:
        choix_rare = st.toggle("Je veux un artiste que j'ai peu écouté.", value=False)
        if choix_rare:
            playlist_musique_selection = playlist_musique_selection[playlist_musique_selection["Nombre d'écoutes"] == playlist_musique_selection["Nombre d'écoutes"].min()]

    liste_artistes = list(playlist_musique_selection['Artiste'].unique())

    if 'artiste_aleatoire' not in st.session_state:
        artiste_aleatoire = random.choice(liste_artistes)
    
    if 'artiste_aleatoire2' not in st.session_state:
        artiste_aleatoire2 = None

    resultat = st.toggle('On lance les dés.', value=False)

    if resultat == True:
        artiste_aleatoire = random.choice(liste_artistes)
        st.markdown(artiste_aleatoire)

        # relancer = st.checkbox('Relancer mon choix.', value=False)

        # if relancer:
        #     playlist_musique_selection2 = playlist_musique_selection[playlist_musique_selection['Artiste'] != artiste_aleatoire]
        #     liste_artistes2 = list(playlist_musique_selection2['Artiste'].unique())
        #     artiste_aleatoire2 = random.choice(liste_artistes2)
        #     st.markdown(artiste_aleatoire2)

        acceptation = st.checkbox('OK je vais écouter ça.')

        # if acceptation:
        #     # Modification des données
        #     playlist_musique.loc[playlist_musique['Artiste'] == artiste_aleatoire, "Nombre d'écoutes"] += 1
        #     # Sauvegarde dans le fichier CSV
        #     playlist_musique.to_csv('BD/playlist_a_jour.csv', index=True)

elif action == 'Un Film':

    choix_genre = st.checkbox('Je veux un genre précis.', value=False)

    if choix_genre:
        liste_genres = list(playlist_film['Genre'].unique())
        liste_genres = [genre for genre in liste_genres if pd.notna(genre)]
        liste_genres.sort()
        genre = st.selectbox('Choisissez le genre:', liste_genres)
        playlist_film_selection = playlist_film_selection[playlist_film_selection['Genre'] == genre]
    
    # if choix_genre: 
    #     genre = st.selectbox('Choisissez le genre:', list(playlist_film['Genre'].unique()))
    #     playlist_film_selection = playlist_film_selection[playlist_film_selection['Genre'] == genre]

    liste_artistes = list(playlist_film_selection['Titre'].unique())

    resultat = st.toggle('On lance les dés.', value=False)

    if resultat == True:
        artiste_aleatoire = random.choice(liste_artistes)
        st.markdown(artiste_aleatoire)

        acceptation = st.checkbox('OK je vais regarder ça.')

        # if acceptation: 
        #     playlist_film = playlist_film[playlist_film['Titre'] != artiste_aleatoire]
        #     playlist_film = playlist_film.sort_values(by=["Titre", "Genre"], ascending=False)
        #     playlist_film.to_csv('BD/films_a_jour.csv', index=True)

elif action == 'Un Livre':
    choix_genre = st.checkbox('Je veux un genre précis.', value=False)

    if choix_genre:
        liste_genres = list(playlist_livre['Genre'].unique())
        liste_genres = [genre for genre in liste_genres if pd.notna(genre)]
        liste_genres.sort()
        genre = st.selectbox('Choisissez le genre:', liste_genres)
        playlist_livre_selection = playlist_livre_selection[playlist_livre_selection['Genre'] == genre]

    liste_artistes = list(playlist_livre_selection['Titre'].unique())

    resultat = st.toggle('On lance les dés.', value=False)

    if resultat == True:
        artiste_aleatoire = random.choice(liste_artistes)
        st.markdown(artiste_aleatoire)

        acceptation = st.checkbox('OK je vais lire ça.')

        # if acceptation:
        #     # Modification des données
        #     playlist_livre = playlist_livre[playlist_livre['Titre'] != artiste_aleatoire]
        #     playlist_livre = playlist_livre.sort_values(by=["Titre", "Genre"], ascending=False)
        #     # Sauvegarde dans le fichier CSV
        #     playlist_livre.to_csv('BD/livres_a_jour.csv', index=True)
