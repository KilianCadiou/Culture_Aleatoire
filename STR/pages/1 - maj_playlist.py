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

actions = ['Je veux ...', 'Ajouter un élément', 'Modifier un élément', 'Supprimer un élément']

action = st.selectbox('Que souhaitez-vous faire ?', actions)

if action == 'Ajouter un élément':

    # # AJOUTER UN GENRE ET UN ARTISTE

    # genre = st.checkbox('Je veux ajouter un genre.')

    # if genre:

    #     ajout_genre_genre = st.text_input('Tapez le genre à ajouter :')

    #     if ajout_genre_genre:
    #         if ajout_genre_genre in playlist['Genre'].unique():
    #             st.markdown('Le genre existe déjà.')
    #         else:

    #             international_artiste = st.toggle("L'artiste est-il français ?", value = False)
    #             if international_artiste == False:
    #                 international = False
    #             else:
    #                 international = True

    #             ajout_artiste_genre = st.text_input("Tapez l'artiste ou le groupe à ajouter :")
    #             if ajout_artiste_genre:
    #                 if ajout_artiste_genre in playlist[playlist['Genre'] == ajout_genre_genre]['Artiste'].unique():
    #                     st.markdown("L'artiste ou le groupe existe déjà.")
    #                 else:
    #                     playlist.loc[len(playlist)] = [ajout_genre_genre, ajout_artiste_genre, international, 0]
    #                     playlist.to_csv('Musique/BD/playlist_a_jour.csv')
    #                     playlist = pd.read_csv('Musique/BD/playlist_a_jour.csv', index_col=0)

    # AJOUTER UN ARTISTE À UN GENRE EXISTANT

    artiste = st.checkbox('Je veux ajouter un artiste ou un groupe.')

    if artiste:
        
        ajout_artiste_artiste = st.text_input("Tapez l'artiste ou le groupe à ajouter :")

        if ajout_artiste_artiste:
            if ajout_artiste_artiste in playlist['Artiste'].unique():
                st.markdown("L'artiste ou le groupe existe déjà.")
            else:
                international_artiste = st.toggle("L'artiste est-il français ?", value = False)
                if international_artiste == False:
                    international = False
                else:
                    international = True

                ajout_genre_artiste = st.text_input('Tapez le genre :')

                if ajout_genre_artiste:
                    playlist.loc[len(playlist)] = [ajout_genre_artiste, ajout_artiste_artiste, international, 0]
                    playlist.to_csv('Musique/BD/playlist_a_jour.csv')
                    playlist = pd.read_csv('Musique/BD/playlist_a_jour.csv', index_col=0)


if action == 'Modifier un élément':
    None

if action == 'Supprimer un élément':

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

    # SUPPRIMER PLAYLIST

    reboot = st.checkbox('Supprimer ma playlist.')

    if reboot:
        reboot2 = st.checkbox('Êtes-vous sûr ?')
        if reboot2:
            playlist = pd.DataFrame(columns=['Genre', 'Artiste', 'Français', "Nombre d'écoutes"])
            playlist.to_csv('Musique/BD/playlist_a_jour.csv')
            playlist = pd.read_csv('Musique/BD/playlist_a_jour.csv', index_col=0)