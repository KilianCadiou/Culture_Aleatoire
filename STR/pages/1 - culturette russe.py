import pandas as pd
import streamlit as st
import warnings
import random
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

playlist_film = pd.read_csv('BD/films_a_jour.csv', index_col=0)
playlist_film_selection = playlist_film.copy()
playlist_musique = pd.read_csv('BD/playlist_a_jour.csv', index_col=0)
playlist_musique_selection = playlist_musique.copy()
playlist_livre = pd.read_csv('BD/livres_a_jour.csv', index_col=0)
playlist_livre_selection = playlist_livre.copy()

st.header('Puisse le sort vous être favorable.')
st.markdown("<hr style='border: 1px solid white; width: 100%;'>", unsafe_allow_html=True)

actions = ['Je veux ...', 'Un Film', 'Une Musique', 'Un Livre']

action = st.selectbox('Que souhaitez-vous faire ?', actions)

if action == 'Un Film':

    choix_genre = st.toggle('Je veux un genre précis.', value = False)

    if choix_genre:

        genre = st.selectbox('Choisissez le genre:', list(playlist_film['Genre'].unique()))
        playlist_film_selection = playlist_film_selection[playlist_film_selection['Genre'] == genre]

    liste_artistes = list(playlist_film_selection['Titre'].unique())

    resultat = st.checkbox('On lance les dés.')

    if resultat:
        artiste_aleatoire = random.choice(liste_artistes)
        st.markdown(artiste_aleatoire)

        relancer = st.toggle('Relancer mon choix.', value = False)

        if relancer:
            artiste_aleatoire = random.choice(liste_artistes)
            st.markdown(artiste_aleatoire)

        acceptation = st.checkbox('OK je vais regarder ça.')
        
        if acceptation:
            playlist_film = playlist_film[playlist_film['Titre'] != artiste_aleatoire]
            playlist_film = playlist_film.sort_values(by = "Titre", ascending = False)
            playlist_film = playlist_film.sort_values(by = "Genre", ascending = False)
            playlist_film.to_csv('BD/films_a_jour.csv')
            playlist_film = pd.read_csv('BD/films_a_jour.csv', index_col=0)

if action == 'Une Musique':
    
    col1, col2, col3 = st.columns(3)

    with col1:

        choix_genre = st.toggle('Je veux un style de musique précis.', value = False)

        if choix_genre:

            genre = st.selectbox('Choisissez le genre:', list(playlist_musique['Genre'].unique()))
            playlist_musique_selection = playlist_musique_selection[playlist_musique_selection['Genre'] == genre]

    with col2:
            
        choix_francais = st.toggle('Je veux de la musique française.', value = False)

        if choix_francais:
            france = st.selectbox('Réponse :', ['Oui', 'Non'])
            if france == 'Oui':
                playlist_musique_selection = playlist_musique_selection[playlist_musique_selection['Français'] == True]
            else:
                playlist_musique_selection = playlist_musique_selection[playlist_musique_selection['Français'] == False]

    with col3:
            
        choix_rare = st.toggle("Je veux un artiste que j'ai peu écouté.", value = False)

        if choix_rare:
            playlist_musique_selection = playlist_musique_selection[playlist_musique_selection["Nombre d'écoutes"] == playlist_musique_selection["Nombre d'écoutes"].min()]

    
    liste_artistes = list(playlist_musique_selection['Artiste'].unique())

    resultat = st.checkbox('On lance les dés.')

    if resultat:
        artiste_aleatoire = random.choice(liste_artistes)
        st.markdown(artiste_aleatoire)

        relancer = st.toggle('Relancer mon choix.', value = False)

        if relancer:
            artiste_aleatoire = random.choice(liste_artistes)
            st.markdown(artiste_aleatoire)
        
        acceptation = st.checkbox('OK je vais écouter ça.')
            
        if acceptation:
            playlist_musique[playlist_musique['Artiste'] == artiste_aleatoire]["Nombre d'écoutes"] = playlist_musique[playlist_musique['Artiste'] == artiste_aleatoire]["Nombre d'écoutes"].apply(lambda x : x + 1)


if action == 'Un Livre':

    choix_genre = st.toggle('Je veux un genre précis.', value = False)

    if choix_genre:

        genre = st.selectbox('Choisissez le genre:', list(playlist_livre['Genre'].unique()))
        playlist = playlist_livre_selection[playlist_livre_selection['Genre'] == genre]

    liste_artistes = list(playlist_livre_selection['Titre'].unique())

    resultat = st.checkbox('On lance les dés.')

    if resultat:
        artiste_aleatoire = random.choice(liste_artistes)
        st.markdown(artiste_aleatoire)

        relancer = st.toggle('Relancer mon choix.', value = False)

        if relancer:
            artiste_aleatoire = random.choice(liste_artistes)
            st.markdown(artiste_aleatoire)

        acceptation = st.checkbox('OK je vais lire ça.')
        
        if acceptation:
            playlist_livre = playlist_livre[playlist_livre['Titre'] != artiste_aleatoire]
            playlist_livre = playlist_livre.sort_values(by = "Titre", ascending = False)
            playlist_livre = playlist_livre.sort_values(by = "Genre", ascending = False)
            playlist_livre.to_csv('BD/livres_a_jour.csv')
            playlist_livre = pd.read_csv('BD/livres_a_jour.csv', index_col=0)

