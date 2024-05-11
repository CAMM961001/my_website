import streamlit as st

from PIL import Image
from .settings import Settings


# Load project settings
settings = Settings()

class SideBar:
    def __init__(self):
        """Initialize sidebar static elements"""
        self.resume = settings.config['path']['resume']
        self.profile = Image.open(settings.config['images']['profile'])
        self.skills = Image.open(settings.config['images']['skills'])



    def profile_picture(self):
        """Function to render profile picture"""
        st.image(self.profile)
    

    def skills_picture(self):
        """Function to render profile picture"""
        st.image(self.skills)


    def download_resume(self):
        """Function to download professional resume"""

        # Open resume file declared in config.yml
        with open(self.resume, 'rb') as file_:
            # Read file
            resume = file_.read()

            # Render download button
            st.download_button(
                label='Download Resume'
                ,data=resume
                ,file_name='miguel_castaneda.pdf'
                ,mime='application/octet-stream'
                ,use_container_width=False)
            
        # Close file
        file_.close()
