import streamlit as st
from st_pages import get_nav_from_toml
import toml

custom_css = """
    <style>
    /* Changer l'arrière-plan de l'application Streamlit */
    .stApp {
        background: linear-gradient(to bottom, rgba(92, 4, 106, 1), rgba(0, 0, 0, 1)) !important;
    }

    /* Modifier l'arrière-plan de la barre latérale */
    section[data-testid="stSidebar"] {
        background: linear-gradient(to bottom, rgba(0, 0, 0, 1), rgba(0, 0, 0, 1)) !important;
    }

    /* Changer la couleur de toutes les polices en blanc dans l'application principale */
    body, .stApp, .stMarkdown, .stText {
        color: white !important;
    }

    /* Changer la couleur du texte dans la sidebar */
    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Optionnel : Ajuster la couleur des titres (si nécessaire) */
    h1, h2, h3, h4, h5, h6 {
        color: white !important;
    }

    /* Optionnel : Ajuster la couleur des liens (si nécessaire) */
    a {
        color: white !important;
    }

        /* Centrer tout le texte */
    .stMarkdown, .stText, .stApp {
        text-align: center !important;
    }

    </style>
"""


st.markdown(custom_css, unsafe_allow_html=True)
st.logo("https://raw.githubusercontent.com/KilianCadiou/Culture_Aleatoire/refs/heads/main/STR/img/DALL%C2%B7E-2025-03-17-14.22.23-Minimalistic-logo-design-for-an-application-called-_Culture-Al%C3%A9atoire_.jpg", size = 'large')



config = toml.load(".streamlit/pages.toml")
print(config)

# nav = get_nav_from_toml("STR/.streamlit/pages.toml")

nav = get_nav_from_toml(".streamlit/pages.toml")

pg = st.navigation(nav)

pg.run()


