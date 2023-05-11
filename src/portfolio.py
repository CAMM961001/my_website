import streamlit as st

from .settings import Settings


# Load project settings
settings = Settings()

class Portfolio:
    def __init__(self):
        self.page_title = 'Portfolio'
        self.descripcion = '''
        Description
        '''
