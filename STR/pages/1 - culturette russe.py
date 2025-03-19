import pandas as pd
import streamlit as st
import warnings
import random
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import json
import streamlit as st

# Filtrage des warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import streamlit as st

def google_drive_auth():
    # Charger les credentials depuis les secrets de Streamlit Cloud
    client_secrets = json.loads(st.secrets["google_drive"]["GOOGLE_DRIVE_CREDENTIALS"])
    
    # Initialiser le flux d'authentification
    flow = InstalledAppFlow.from_client_config(client_secrets, scopes=["https://www.googleapis.com/auth/drive"])
    creds = flow.run_local_server(port=0)
    
    # Authentifier et créer un service Google Drive
    drive = GoogleDrive(creds)
    return drive

# Télécharger un fichier CSV depuis Google Drive
def download_csv(file_id, local_filename):
    drive = google_drive_auth()
    downloaded = drive.CreateFile({'id': file_id})
    downloaded.GetContentFile(local_filename)
    df = pd.read_csv(local_filename)
    return df

# Uploader un fichier CSV sur Google Drive
def upload_csv(file_id, local_filename):
    drive = google_drive_auth()
    upload_file = drive.CreateFile({'id': file_id})
    upload_file.SetContentFile(local_filename)
    upload_file.Upload()

# Fonction principale de gestion de l'interface Streamlit

st.title("Gestion des CSV avec Google Drive")

# ID des fichiers CSV sur Google Drive
file_ids = {
    'films': '1qVgY-V1j6BK83ZGG76zD-fHHjfvOevJB',
    'musique': '1qXWSjoCfCYbKfz58wlad_hKF4moyjZZC',
    'livres': '1qXPsMDfihJMkPyr0Z2xi-X6fJP5hlUza'
}

# Télécharger les CSV depuis Google Drive
st.write("Téléchargement du fichier CSV...")
film_df = download_csv(file_ids['films'], 'films_a_jour.csv')
musique_df = download_csv(file_ids['musique'], 'playlist_a_jour.csv')
livre_df = download_csv(file_ids['livres'], 'livres_a_jour.csv')

st.write(film_df.head())

# Modifier le CSV de films
if st.button("Modifier le fichier CSV Films"):
    film_df['Titre'] = film_df['Titre'].str.upper()  # Exemple de modification
    film_df.to_csv('films_a_jour.csv', index=False)
    st.write("Fichier films modifié !")

# Ré-uploader le fichier CSV de films modifié
if st.button("Uploader le fichier modifié Films sur Google Drive"):
    upload_csv(file_ids['films'], 'films_a_jour.csv')
    st.write("Fichier films mis à jour sur Google Drive !")

# Choisir l'action souhaitée
actions = ['Je veux ...', 'Un Film', 'Une Musique', 'Un Livre']
action = st.selectbox('Que souhaitez-vous faire ?', actions)

# Processus pour choisir un film
if action == 'Un Film':
    playlist_film_selection = film_df.copy()
    choix_genre = st.checkbox('Je veux un genre précis.', value=False)
    if choix_genre:
        genre = st.selectbox('Choisissez le genre:', list(playlist_film_selection['Genre'].unique()))
        playlist_film_selection = playlist_film_selection[playlist_film_selection['Genre'] == genre]
    
    liste_artistes = list(playlist_film_selection['Titre'].unique())
    resultat = st.checkbox('On lance les dés.')
    
    if resultat:
        artiste_aleatoire = random.choice(liste_artistes)
        st.markdown(artiste_aleatoire)
        
        if st.checkbox('Relancer mon choix.', value=False):
            artiste_aleatoire = random.choice(liste_artistes)
            st.markdown(artiste_aleatoire)
        
        if st.checkbox('OK je vais regarder ça.'):
            playlist_film_selection = playlist_film_selection[playlist_film_selection['Titre'] != artiste_aleatoire]
            playlist_film_selection = playlist_film_selection.sort_values(by=["Titre", "Genre"], ascending=False)
            playlist_film_selection.to_csv('films_a_jour.csv', index=False)
            upload_csv(file_ids['films'], 'films_a_jour.csv')

# Processus pour choisir de la musique
if action == 'Une Musique':
    playlist_musique_selection = musique_df.copy()
    col1, col2, col3 = st.columns(3)

    with col1:
        choix_genre = st.checkbox('Je veux un style de musique précis.', value=False)
        if choix_genre:
            genre = st.selectbox('Choisissez le genre:', list(playlist_musique_selection['Genre'].unique()))
            playlist_musique_selection = playlist_musique_selection[playlist_musique_selection['Genre'] == genre]

    with col2:
        choix_francais = st.checkbox('Je veux de la musique française.', value=False)
        if choix_francais:
            france = st.selectbox('Réponse :', ['Oui', 'Non'])
            if france == 'Oui':
                playlist_musique_selection = playlist_musique_selection[playlist_musique_selection['Français'] == True]
            else:
                playlist_musique_selection = playlist_musique_selection[playlist_musique_selection['Français'] == False]

    with col3:
        choix_rare = st.checkbox("Je veux un artiste que j'ai peu écouté.", value=False)
        if choix_rare:
            playlist_musique_selection = playlist_musique_selection[playlist_musique_selection["Nombre d'écoutes"] == playlist_musique_selection["Nombre d'écoutes"].min()]

    liste_artistes = list(playlist_musique_selection['Artiste'].unique())
    resultat = st.checkbox('On lance les dés.')

    if resultat:
        artiste_aleatoire = random.choice(liste_artistes)
        st.markdown(artiste_aleatoire)

        if st.checkbox('Relancer mon choix.', value=False):
            playlist_musique_selection = playlist_musique_selection[playlist_musique_selection['Artiste'] != artiste_aleatoire]
            liste_artistes = list(playlist_musique_selection['Artiste'].unique())
            artiste_aleatoire = random.choice(liste_artistes)
            st.markdown(artiste_aleatoire)

        if st.checkbox('OK je vais écouter ça.'):
            musique_df.loc[musique_df['Artiste'] == artiste_aleatoire, "Nombre d'écoutes"] += 1
            musique_df.to_csv('playlist_a_jour.csv', index=False)
            upload_csv(file_ids['musique'], 'playlist_a_jour.csv')

# Processus pour choisir un livre
if action == 'Un Livre':
    playlist_livre_selection = livre_df.copy()
    choix_genre = st.checkbox('Je veux un genre précis.', value=False)
    if choix_genre:
        genre = st.selectbox('Choisissez le genre:', list(playlist_livre_selection['Genre'].unique()))
        playlist_livre_selection = playlist_livre_selection[playlist_livre_selection['Genre'] == genre]
    
    liste_artistes = list(playlist_livre_selection['Titre'].unique())
    resultat = st.checkbox('On lance les dés.')

    if resultat:
        artiste_aleatoire = random.choice(liste_artistes)
        st.markdown(artiste_aleatoire)

        if st.checkbox('Relancer mon choix.', value=False):
            artiste_aleatoire = random.choice(liste_artistes)
            st.markdown(artiste_aleatoire)

        if st.checkbox('OK je vais lire ça.'):
            livre_df = livre_df[livre_df['Titre'] != artiste_aleatoire]
            livre_df = livre_df.sort_values(by=["Titre", "Genre"], ascending=False)
            livre_df.to_csv('livres_a_jour.csv', index=False)
            upload_csv(file_ids['livres'], 'livres_a_jour.csv')
