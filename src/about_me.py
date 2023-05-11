import streamlit as st

from .settings import Settings


# Load project settings
settings = Settings()

class AboutMe:
    def __init__(self):
        self.page_title = 'About Me'
        self.descripcion = '''
        Description
        '''
