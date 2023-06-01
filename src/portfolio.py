import json
import streamlit as st

from .settings import Settings
from .utils import render_button
from PIL import Image


# Load project settings
settings = Settings()

class Portfolio:
    def __init__(self):
        self.page_title = 'Portfolio'
        with open(settings.config['path']['portfolio']) as file_:
            self.data = json.load(file_)
        file_.close()


    def render_project(
            self
            ,name: str
            ,contrib: list
            ,desc: str
            ,img_path: str
            ,site_url: str
            ,src_url: str):
        
        # Project header and cortibutors
        st.subheader(name)
        st.caption(', '.join(contrib))

        # Project cover image
        cover = Image.open(img_path)
        st.image(cover)

        # Project description
        desc = f'''<p style="text-align: justify">{desc}</p>'''
        st.write(desc, unsafe_allow_html=True)

        # Project navigation buttons
        render_button(url=site_url)
        render_button(url=src_url, name='Source')
