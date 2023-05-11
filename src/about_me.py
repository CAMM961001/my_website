import pandas as pd
import streamlit as st

from PIL import Image
from .settings import Settings


# Load project settings
settings = Settings()

class AboutMe:
    def __init__(self):
        self.page_title = 'About Me'
        self.today = pd.Timestamp.today().date()
        self.description = [
        """
        <p style="text-align: justify; font-size: {settings.fontsize}px">
            <br>
            I am a data scientist experienced in manufacturing processes, and 
            automation of financial services back-end processes. My specialization 
            covers end-to-end data analytics solutions, from data engineering to 
            Business Intelligence. I am interested on professional challenges 
            involving Machine Learning and Statistical Modeling to leverage 
            data-driven decisions.
            </br>
        </p>""",
        """
        <p style="text-align: justify; font-size: {settings.fontsize}px">
            <br>
            Description
            </br>
        </p>
        """,
        """
        <p style="text-align: justify; font-size: {settings.fontsize}px">
            <br>
            If my techinal skills were a first person shooter videogame, I would
            play them in the following skill level:
            </br>
        </p>
        """
        ]
    

    def timeline(self):
        # Section header
        st.header('Timeline')

        # Section description
        st.write(self.description[1], unsafe_allow_html=True)

        # Load previously generated image
        fig_ = Image.open(settings.config['images']['timeline'])

        # Render image
        st.image(fig_)


    def skills(self):
        # Section header
        st.header('Technology Stack')

        # Section description
        st.write(self.description[2], unsafe_allow_html=True)
        
        with st.container():
            col1, col2 = st.columns((1,1))

            with col1:
                # Load previously generated image
                fig_ = Image.open(settings.config['images']['analytics'])

                # Render image
                st.image(fig_)
            
            with col2:
                # Load previously generated image
                fig_ = Image.open(settings.config['images']['development'])

                # Render image
                st.image(fig_)

        with st.container():
            col1, col2 = st.columns((1,1))

            with col1:
                # Load previously generated image
                fig_ = Image.open(settings.config['images']['bi'])

                # Render image
                st.image(fig_)
            
            with col2:
                # Load previously generated image
                fig_ = Image.open(settings.config['images']['cloud'])

                # Render image
                st.image(fig_)
        
        st.write("###")
