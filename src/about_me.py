import streamlit as st

from .settings import Settings


# Load project settings
settings = Settings()

class AboutMe:
    def __init__(self):
        self.page_title = 'About Me'
        self.descripcion = '''
        <p style="text-align: justify; font-size: {settings.fontsize}px">
            <br>
            I am a data scientist experienced in manufacturing processes, and 
            automation of financial services back-end processes. My specialization 
            covers end-to-end data analytics solutions, from data engineering to 
            Business Intelligence. I am interested on professional challenges 
            involving Machine Learning and Statistical Modeling to leverage 
            data-driven decisions.
            </br>
        </p>
        '''
