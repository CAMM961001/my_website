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
            self.data = json.load(file_)['projects']
        file_.close()


    def first_row(self):
        with st.container():
            col1, col2, col3= st.columns(3, gap='large')

            with col1:
                # Project header and cortibutors
                st.subheader(self.data[0]['project_name'])
                st.caption(self.data[0]['contributors'])
                
                # Project cover image
                cover = Image.open(self.data[0]['cover'])
                st.image(cover)

                # Project description content
                description = ""
                for line in self.data[0]['description']:
                    description += line
                description = f'''<p style="text-align: justify">{description}</p>'''

                # Render description
                st.write(description, unsafe_allow_html=True)

                # Project navigation buttons
                render_button(url=self.data[0]['site_url'])
                render_button(url=self.data[0]['source_url'], name='View source')