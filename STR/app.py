import streamlit as st
from st_pages import get_nav_from_toml
import toml

st.logo("Culture_Aleatoire/STR/img/DALL·E-2025-03-17-14.22.23-Minimalistic-logo-design-for-an-application-called-_Culture-Aléatoire_.jpg", size = 'large')

config = toml.load("Culture_Aleatoire/STR/.streamlit/pages.toml")
print(config)

# nav = get_nav_from_toml("STR/.streamlit/pages.toml")

nav = get_nav_from_toml("Culture_Aleatoire/STR/.streamlit/pages.toml")

pg = st.navigation(nav)

pg.run()


