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
        contrib = [
            f'''<a
            href="{list(cont.values())[0]}"
            style="
                color: {settings.toml_config["theme"]["socialMediaColor"]};
                text-decoration:none;
                font-weight:bold">{list(cont.keys())[0]}</a>'''
        for cont in contrib]
        st.caption(body=', '.join(contrib), unsafe_allow_html=True)

        # Project cover image
        cover = Image.open(img_path)
        st.image(cover)

        # Project description
        desc = f'''<p style="text-align: justify">{desc}</p>'''
        st.write(desc, unsafe_allow_html=True)

        # Project navigation buttons
        render_button(url=site_url)
        st.write('')
        render_button(url=src_url, name='Source')
