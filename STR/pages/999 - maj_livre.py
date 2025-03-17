import pandas as pd
import streamlit as st
import warnings
import random
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

playlist = pd.read_csv('Culture_Aleatoire/BD/livres_a_jour.csv', index_col=0)

actions = ['Je veux ...', 'Ajouter un élément', 'Modifier un élément', 'Supprimer un élément']

action = st.selectbox('Que souhaitez-vous faire ?', actions)

if action == 'Ajouter un élément':

    # AJOUTER UN FILM

    artiste = st.checkbox('Je veux ajouter un livre.')

    if artiste:
        
        ajout_artiste_artiste = st.text_input("Tapez le livre à ajouter :")

        if ajout_artiste_artiste:
            if ajout_artiste_artiste in playlist['Titre'].unique():
                st.markdown("Le livre existe déjà.")
            else:

                ajout_genre_artiste = st.text_input('Tapez le genre :')

                if ajout_genre_artiste:
                    playlist.loc[len(playlist)] = [ajout_genre_artiste, ajout_artiste_artiste]
                    playlist.to_csv('Culture_Aleatoire/BD/livres_a_jour.csv')
                    playlist = pd.read_csv('Culture_Aleatoire/BD/livres_a_jour.csv', index_col=0)


if action == 'Modifier un élément':
    None

if action == 'Supprimer un élément':

    # SUPPRIMER UN ARTISTE

    supprimer = st.checkbox('Je veux supprimer un livre.')

    if supprimer:
        suppr_artiste = st.text_input("Tapez le nom du livre :")
        if suppr_artiste:
            if suppr_artiste not in playlist['Titre'].unique():
                st.markdown("Le livre n'est pas dans la liste.")
            else:
                playlist = playlist[playlist['Titre'] != suppr_artiste]
                playlist.to_csv('Culture_Aleatoire/BD/livres_a_jour.csv')
                playlist = pd.read_csv('Culture_Aleatoire/BD/livres_a_jour.csv', index_col=0)

    # SUPPRIMER PLAYLIST

    reboot = st.checkbox('Supprimer ma liste de livres.')

    if reboot:
        reboot2 = st.checkbox('Êtes-vous sûr ?')
        if reboot2:
            playlist = pd.DataFrame(columns=['Genre', 'Titre'])
            playlist.to_csv('Culture_Aleatoire/BD/livres_a_jour.csv')
            playlist = pd.read_csv('Culture_Aleatoire/BD/livres_a_jour.csv', index_col=0)

voir = st.checkbox('Voir ma liste de livres.')

if voir:
    st.dataframe(playlist)