import pandas as pd
import streamlit as st
import warnings
import random
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

playlist = pd.read_csv('Culture_Aleatoire/BD/playlist_a_jour.csv', index_col=0)

# PROPOSITION ARTISTE

st.header('Choix Artiste')

col1, col2, col3 = st.columns(3)

with col1:
    choix_genre = st.toggle('Je veux un genre précis.', value = False)

    if choix_genre:

        genre = st.selectbox('Choisissez le genre:', list(playlist['Genre'].unique()))
        playlist = playlist[playlist['Genre'] == genre]

with col2:
        
    choix_francais = st.toggle('Je veux de la musique française.', value = False)

    if choix_francais:
        france = st.selectbox('Réponse :', ['Oui', 'Non'])
        if france == 'Oui':
            playlist = playlist[playlist['Français'] == True]
        else:
            playlist = playlist[playlist['Français'] == False]

with col3:
        
    choix_rare = st.toggle("Je veux un artiste que j'ai peu écouté.", value = False)

    if choix_rare:
        playlist = playlist[playlist["Nombre d'écoutes"] == playlist["Nombre d'écoutes"].min()]

proposition = st.checkbox('Propose moi un artiste')

if proposition:
    liste_artistes = list(playlist['Artiste'].unique())
    artiste_aleatoire = random.choice(liste_artistes)
    st.markdown(artiste_aleatoire)

    acceptation = st.checkbox('OK je vais écouter ça.')
    
    if acceptation:
        playlist[playlist['Artiste'] == artiste_aleatoire]["Nombre d'écoutes"] = playlist[playlist['Artiste'] == artiste_aleatoire]["Nombre d'écoutes"].apply(lambda x : x + 1)
