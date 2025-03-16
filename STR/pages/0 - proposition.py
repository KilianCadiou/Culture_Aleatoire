import pandas as pd
import streamlit as st
import warnings
import random
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

playlist = pd.read_csv('Musique/BD/playlist_a_jour.csv', index_col=0)

voir = st.checkbox('Voir ma playlist.')

if voir:
    st.dataframe(playlist)

st.header("👇 Créer une liste de musique :")

# AJOUTER UN GENRE ET UN ARTISTE

genre = st.checkbox('Je veux ajouter un genre.')

if genre:

    ajout_genre_genre = st.text_input('Tapez le genre à ajouter :')

    if ajout_genre_genre:
        if ajout_genre_genre in playlist['Genre'].unique():
            st.markdown('Le genre existe déjà.')
        else:

            international_artiste = st.toggle("L'artiste est-il français ?", value = False)
            if international_artiste == False:
                international = False
            else:
                international = True

            ajout_artiste_genre = st.text_input("Tapez l'artiste ou le groupe à ajouter :")
            if ajout_artiste_genre:
                if ajout_artiste_genre in playlist[playlist['Genre'] == ajout_genre_genre]['Artiste'].unique():
                    st.markdown("L'artiste ou le groupe existe déjà.")
                else:
                    playlist.loc[len(playlist)] = [ajout_genre_genre, ajout_artiste_genre, international, 0]
                    playlist.to_csv('Musique/BD/playlist_a_jour.csv')
                    playlist = pd.read_csv('Musique/BD/playlist_a_jour.csv', index_col=0)

# AJOUTER UN ARTISTE À UN GENRE EXISTANT

artiste = st.checkbox('Je veux ajouter un artiste ou un groupe.')

if artiste:

    ajout_genre_artiste = st.text_input('Tapez le genre :')

    if ajout_genre_artiste:
        if ajout_genre_artiste not in playlist['Genre'].unique():
            st.markdown("Le genre n'existe pas.")
        else:

            international_artiste = st.toggle("L'artiste est-il français ?", value = False)
            if international_artiste == False:
                international = False
            else:
                international = True

            ajout_artiste_artiste = st.text_input("Tapez l'artiste ou le groupe à ajouter :")

            if ajout_artiste_artiste:
                if ajout_artiste_artiste in playlist[playlist['Genre'] == ajout_genre_artiste]['Artiste'].unique():
                    st.markdown("L'artiste ou le groupe existe déjà.")
                else:
                    playlist.loc[len(playlist)] = [ajout_genre_artiste, ajout_artiste_artiste, international, 0]
                    playlist.to_csv('Musique/BD/playlist_a_jour.csv')
                    playlist = pd.read_csv('Musique/BD/playlist_a_jour.csv', index_col=0)

    st.dataframe(playlist)


# SUPPRIMER UN ARTISTE

supprimer = st.checkbox('Je veux supprimer un artiste ou un groupe.')

if supprimer:
    suppr_artiste = st.text_input("Tapez le nom de l'artiste ou du groupe :")
    if suppr_artiste:
        if suppr_artiste not in playlist['Artiste'].unique():
            st.markdown("L'artiste ou le groupe n'est pas dans la playlist.")
        else:
            playlist = playlist[playlist['Artiste'] != suppr_artiste]
            playlist.to_csv('Musique/BD/playlist_a_jour.csv')
            playlist = pd.read_csv('Musique/BD/playlist_a_jour.csv', index_col=0)

# PROPOSITION ARTISTE

st.header('Choix Artiste')

choix_genre = st.toggle('Je veux un genre précis.')

if choix_genre:
    playlist = playlist[playlist['Genre'] == choix_genre]

choix_francais = st.toggle('Je veux de la musique française.')

if choix_francais:
    playlist = playlist[playlist['Français'] == choix_francais]

choix_rare = st.toggle("Je veux un artiste que j'ai peu écouté.")
if choix_rare:
    playlist = playlist[playlist["Nombre d'écoutes"] == playlist["Nombre d'écoutes"].min()]

proposition = st.checkbox('Propose moi un artiste')

if proposition:
    liste_artistes = list(playlist['Artiste'].unique())
    artiste_aleatoire = random.choice(liste_artistes)
    playlist[playlist['Artiste'] == artiste_aleatoire]["Nombre d'écoutes"] = playlist[playlist['Artiste'] == artiste_aleatoire]["Nombre d'écoutes"].apply(lambda x : x + 1)
    st.markdown(artiste_aleatoire)

reboot = st.checkbox('Supprimer ma playlist.')

if reboot:
    reboot2 = st.checkbox('Êtes-vous sûr ?')
    if reboot2:
        playlist = pd.DataFrame(columns=['Genre', 'Artiste', 'Français', "Nombre d'écoutes"])
        playlist.to_csv('Musique/BD/playlist_a_jour.csv')
        playlist = pd.read_csv('Musique/BD/playlist_a_jour.csv', index_col=0)