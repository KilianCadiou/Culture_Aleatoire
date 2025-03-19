import pandas as pd
import streamlit as st
import warnings
import random
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

import os
import gdown
import pandas as pd

def upload_csv(file_id, local_filename):
    upload_file = drive.CreateFile({'id': file_id})
    upload_file.SetContentFile(local_filename)
    upload_file.Upload()


# Créer le dossier BD s'il n'existe pas
if not os.path.exists('BD'):
    os.makedirs('BD')

# === FILMS ===
film_url = 'https://drive.google.com/file/d/1qVgY-V1j6BK83ZGG76zD-fHHjfvOevJB/view?usp=sharing'
film_csv_path = 'BD/films_a_jour.csv'
if not os.path.exists(film_csv_path):
    gdown.download(film_url, film_csv_path, quiet=False)

playlist_film = pd.read_csv(film_csv_path, index_col=0)

# === MUSIQUE ===
musique_url = 'https://drive.google.com/file/d/1qXWSjoCfCYbKfz58wlad_hKF4moyjZZC/view?usp=sharing'
musique_csv_path = 'BD/playlist_a_jour.csv'
if not os.path.exists(musique_csv_path):
    gdown.download(musique_url, musique_csv_path, quiet=False)

playlist_musique = pd.read_csv(musique_csv_path, index_col=0)

# === LIVRES ===
livre_url = 'https://drive.google.com/file/d/1qXPsMDfihJMkPyr0Z2xi-X6fJP5hlUza/view?usp=sharing'
livre_csv_path = 'BD/livres_a_jour.csv'
if not os.path.exists(livre_csv_path):
    gdown.download(livre_url, livre_csv_path, quiet=False)

playlist_livre = pd.read_csv(livre_csv_path, index_col=0)

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pandas as pd
import streamlit as st
import os

# Authentification
def google_drive_auth():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()  # Lancement du serveur local pour authentification
    drive = GoogleDrive(gauth)
    return drive

drive = google_drive_auth()

def download_csv(file_id, local_filename):
    downloaded = drive.CreateFile({'id': file_id})
    downloaded.GetContentFile(local_filename)
    df = pd.read_csv(local_filename)
    return df

file_id = '1qVgY-V1j6BK83ZGG76zD-fHHjfvOevJB'
local_file = 'films_a_jour.csv'
playlist_film = download_csv(file_id, local_file)

file_id = '1qXWSjoCfCYbKfz58wlad_hKF4moyjZZC'
local_file = 'playlist_a_jour.csv'
playlist_musique = download_csv(file_id, local_file)

file_id = '1qXPsMDfihJMkPyr0Z2xi-X6fJP5hlUza'
local_file = 'livres_a_jour.csv'
playlist_livre = download_csv(file_id, local_file)

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

            playlist_film.to_csv('films_a_jour.csv', index=False)
            upload_csv("1qVgY-V1j6BK83ZGG76zD-fHHjfvOevJB", 'films_a_jour.csv')

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
            playlist_musique_selection = playlist_musique_selection[playlist_musique_selection['Artiste'] != artiste_aleatoire]
            liste_artistes = list(playlist_musique_selection['Artiste'].unique())
            artiste_aleatoire = random.choice(liste_artistes)
            st.markdown(artiste_aleatoire)
        
        acceptation = st.checkbox('OK je vais écouter ça.')
            
        if acceptation:
            playlist_musique[playlist_musique['Artiste'] == artiste_aleatoire]["Nombre d'écoutes"] = playlist_musique[playlist_musique['Artiste'] == artiste_aleatoire]["Nombre d'écoutes"].apply(lambda x : x + 1)

            playlist_musique.to_csv('playlist_a_jour.csv', index=False)
            upload_csv('1qXWSjoCfCYbKfz58wlad_hKF4moyjZZC', 'playlist_a_jour.csv')


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
            playlist_livre.to_csv('livres_a_jour.csv', index=False)
            upload_csv("1qXPsMDfihJMkPyr0Z2xi", "livres_a_jour.csv")