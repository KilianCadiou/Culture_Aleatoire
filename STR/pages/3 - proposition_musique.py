import pandas as pd
import streamlit as st
import warnings
import random
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

playlist = pd.read_csv('BD/playlist_a_jour.csv', index_col=0)
playlist = playlist.sort_values(by = "Artiste", ascending = False)
playlist = playlist.sort_values(by = "Français", ascending = False)
playlist = playlist.sort_values(by = "Genre", ascending = False)

# PROPOSITION ARTISTE

# st.header('Choix Artiste')
# st.markdown("<hr style='border: 1px solid white; width: 100%;'>", unsafe_allow_html=True)
# col1, col2, col3 = st.columns(3)

# with col1:
#     choix_genre = st.toggle('Je veux un style de musique précis.', value = False)

#     if choix_genre:

#         genre = st.selectbox('Choisissez le genre:', list(playlist['Genre'].unique()))
#         playlist = playlist[playlist['Genre'] == genre]

# with col2:
        
#     choix_francais = st.toggle('Je veux de la musique française.', value = False)

#     if choix_francais:
#         france = st.selectbox('Réponse :', ['Oui', 'Non'])
#         if france == 'Oui':
#             playlist = playlist[playlist['Français'] == True]
#         else:
#             playlist = playlist[playlist['Français'] == False]

# with col3:
        
#     choix_rare = st.toggle("Je veux un artiste que j'ai peu écouté.", value = False)

#     if choix_rare:
#         playlist = playlist[playlist["Nombre d'écoutes"] == playlist["Nombre d'écoutes"].min()]

# proposition = st.checkbox('Propose moi un artiste')

# if proposition:
#     liste_artistes = list(playlist['Artiste'].unique())
#     artiste_aleatoire = random.choice(liste_artistes)
#     st.markdown(artiste_aleatoire)

#     acceptation = st.checkbox('OK je vais écouter ça.')
    
#     if acceptation:
#         playlist[playlist['Artiste'] == artiste_aleatoire]["Nombre d'écoutes"] = playlist[playlist['Artiste'] == artiste_aleatoire]["Nombre d'écoutes"].apply(lambda x : x + 1)

# st.markdown("<br><br>", unsafe_allow_html=True)


st.header('Mettre à jour ma playlist.')
st.markdown("<hr style='border: 1px solid white; width: 100%;'>", unsafe_allow_html=True)
actions = ['Je veux ...', 'Ajouter un élément', 'Modifier un élément', 'Supprimer un élément']

action = st.selectbox('Que souhaitez-vous faire ?', actions)

if action == 'Ajouter un élément':

    # AJOUTER UN ARTISTE

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
                    playlist = playlist.sort_values(by = "Artiste", ascending = False)
                    playlist = playlist.sort_values(by = "Français", ascending = False)
                    playlist = playlist.sort_values(by = "Genre", ascending = False)
                    playlist.to_csv('BD/playlist_a_jour.csv')
                    playlist = pd.read_csv('BD/playlist_a_jour.csv', index_col=0)


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
                playlist = playlist.sort_values(by = "Artiste", ascending = False)
                playlist = playlist.sort_values(by = "Français", ascending = False)
                playlist = playlist.sort_values(by = "Genre", ascending = False)
                playlist.to_csv('BD/playlist_a_jour.csv')
                playlist = pd.read_csv('BD/playlist_a_jour.csv', index_col=0)

    # SUPPRIMER PLAYLIST

    reboot = st.checkbox('Supprimer ma playlist.')

    if reboot:
        reboot2 = st.checkbox('Êtes-vous sûr ?')
        if reboot2:
            playlist = pd.DataFrame(columns=['Genre', 'Artiste', 'Français', "Nombre d'écoutes"])
            playlist = playlist.sort_values(by = "Artiste", ascending = False)
            playlist = playlist.sort_values(by = "Français", ascending = False)
            playlist = playlist.sort_values(by = "Genre", ascending = False)
            playlist.to_csv('BD/playlist_a_jour.csv')
            playlist = pd.read_csv('BD/playlist_a_jour.csv', index_col=0)

voir = st.checkbox('Voir ma playlist.')

if voir:
    st.dataframe(playlist)