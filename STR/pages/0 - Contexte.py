import pandas as pd
import streamlit as st
import warnings
import random
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

col1, col2 = st.columns(2)

with col1:

    st.image('Culture_Aleatoire/STR/img/DALL·E-2025-03-17-14.28.jpg', use_container_width=True)

with col2:
    st.markdown("Pourquoi ai-je créé cette page ?")

    st.markdown("J'ai toujours eu tendance à noter le nom d'artistes, de films ou de livres que je découvre.")

    st.markdown("Toutefois, je les oublie, je ne les regarde pas, je me perds dans mes listes.")

    st.markdown("Ici je centralise ce que je découvre et les garde à disposition.")

    st.markdown("Grâce à cette petite application, je peux choisir aléatoirement ce que je vais écouter / regarder / lire.")

    st.markdown("Je ne dépends de personne d'autre que de moi-même. Je crée et gère mes propres listes.")