import streamlit as st
from st_pages import get_nav_from_toml
import toml
import pandas as pd
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

# Authentification Google Drive
def google_drive_auth():
    gauth = GoogleAuth()
    
    # Authentification locale Streamlit Cloud (via les secrets)
    gauth.LoadCredentialsFile(os.getenv('GOOGLE_DRIVE_CREDENTIALS'))
    if gauth.credentials is None:
        gauth.LocalWebserverAuth()  # Lancement du serveur local pour authentification
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()

    gauth.SaveCredentialsFile(os.getenv('GOOGLE_DRIVE_CREDENTIALS'))
    drive = GoogleDrive(gauth)
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

# Fonction de gestion de l'interface Streamlit
def main():
    st.title("Gestion des CSV avec Google Drive")
    
    # ID du fichier CSV sur Google Drive (tu dois l'extraire de l'URL Google Drive)
    file_id = 'TON_ID_CSV'
    
    # Télécharger le CSV
    st.write("Téléchargement du fichier CSV...")
    df = download_csv(file_id, 'films_a_jour.csv')
    st.write(df.head())
    
    # Modifier le CSV
    if st.button("Modifier le fichier CSV"):
        df['Titre'] = df['Titre'].str.upper()  # Exemple de modification
        df.to_csv('films_a_jour.csv', index=False)
        st.write("Fichier modifié !")
    
    # Ré-uploader le fichier CSV modifié
    if st.button("Uploader le fichier modifié sur Google Drive"):
        upload_csv(file_id, 'films_a_jour.csv')
        st.write("Fichier mis à jour sur Google Drive !")
        
if __name__ == "__main__":
    main()

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



config = toml.load("STR/.streamlit/pages.toml")
print(config)

# nav = get_nav_from_toml("STR/.streamlit/pages.toml")

nav = get_nav_from_toml("STR/.streamlit/pages.toml")

pg = st.navigation(nav)

pg.run()


