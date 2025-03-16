import streamlit as st
from st_pages import get_nav_from_toml
import toml

config = toml.load("STR/.streamlit/pages.toml")
print(config)

# nav = get_nav_from_toml("STR/.streamlit/pages.toml")

nav = get_nav_from_toml("STR/.streamlit/pages.toml")

pg = st.navigation(nav)

pg.run()


