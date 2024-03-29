import os
import pandas as pd
import streamlit as st

from PIL import Image
from .settings import Settings


# Load project settings
settings = Settings()
{settings.toml_config["theme"]["socialMediaColor"]}
class AboutMe:
    def __init__(self):
        self.today = pd.Timestamp.today().date()
        # Site URL to other pages
        self.ITAM = f'<a href="https://mcdatos.itam.mx/es" style="color: {settings.toml_config["theme"]["socialMediaColor"]}; text-decoration:none; font-weight:bold">ITAM</a>'
        self.INAI = f'<a href="https://home.inai.org.mx/" style="color: {settings.toml_config["theme"]["socialMediaColor"]}; text-decoration:none; font-weight:bold">INAI</a>'
        self.CDAS = f'<a href="https://www.facebook.com/dataalgosocitam/" style="color: {settings.toml_config["theme"]["socialMediaColor"]}; text-decoration:none; font-weight:bold">CDAS</a>'
        self.PROSS  = f'<a href="https://ppross.mx/" style="color: {settings.toml_config["theme"]["socialMediaColor"]}; text-decoration:none; font-weight:bold">Procesos PROSS</a>'
        self.BILSTEIN =  f'<a href="https://bilstein.com/en-us/about-us/" style="color: {settings.toml_config["theme"]["socialMediaColor"]}; text-decoration:none; font-weight:bold">Bilstein Shock Absorbers</a>'
        self.FSAE = f'<a href="https://www.fsaeonline.com/" style="color: {settings.toml_config["theme"]["socialMediaColor"]}; text-decoration:none; font-weight:bold">FSAE</a>'
        self.UNAM = f'<a href="http://www.fi-a.unam.mx/" style="color: {settings.toml_config["theme"]["socialMediaColor"]}; text-decoration:none; font-weight:bold">UNAM School of Engineering</a>'
        self.UNAMMS = f'<a href="https://unam.pro/" style="color: {settings.toml_config["theme"]["socialMediaColor"]}; text-decoration:none; font-weight:bold">UNAM Motorsports</a>'
        self.LIVERPOOL = f'<a href="https://www.elpuertodeliverpool.mx/" style="color: {settings.toml_config["theme"]["socialMediaColor"]}; text-decoration:none; font-weight:bold">El Puerto de Liverpool</a>'

        # Site content
        self.description = [
        f"""
        <p style="text-align: justify;">
            First of all, thank you for taking the time to visit my personal website,
            here you'll be able to get to know me a bit more, about my background, 
            and some of my personal projects which, for obvious reasons, are based 
            on open data sources and technology. That being said, this site is not 
            intended to be just another boring resume (or JABR as a like to call it),
            though I am kind enough to leave you a really pretty button in the left sidebar 
            to download it if that's what you're looking for.
            </br>
            <br>
            Moving on, I'm a Data Scientist experienced in manufacturing processes, 
            financial services, and retail industry, currently working at {self.LIVERPOOL}
            which is one of the biggest retailers in Mexico. My specialization 
            covers end-to-end data science solutions, from data engineering to 
            end-user dashboards and storytelling. I'm interested in professional 
            challenges involving Machine Learning and Statistical Modeling.
            </br>
            <br>
            I'm a recent graduate from the MSc. in Data Science at {self.ITAM}, 
            where I volunteered as Data Scientist with {self.INAI} (Mexico's 
            National Institute for Information Accessibility and Transparency) through 
            {self.CDAS}, which is ITAM's extracurricular organization responsible for 
            tackling diverse social topics powered by data analytics.
            </br>
            <br>
            Prior to this, I worked at {self.PROSS} initially as Compliance Analyst and 
            then as Project Manager for a year and a half. Before that, I perfomed an 
            engineering role with the Manufacturing Process Plan Team at {self.BILSTEIN}. 
            In addition, during my Bachelor in Mechanical Engineering at {self.UNAM}, I 
            participated during four years in the {self.FSAE} design series with {self.UNAMMS}, 
            which is a really cool project and I strongly encourage you to visit it.
            </br>
        </p>"""]
    

    def timeline(self):
        # Load previously generated image
        fig_ = Image.open(settings.config['images']['timeline'])

        # Render image
        st.image(fig_, caption='Build with Python')

    
    def side_images(self):
        # Path to pictures directory
        jpg_dir = os.path.join(settings.ROOT, 'images/pictures')

        # Caption of the images
        caption = [
            'UM46-7 Vehicle Rollout Event, 2016'
            ,'Formula ATA Italy, 2017'
            ,'Formula SAE Lincoln, 2018'
            ,'UM10 Kickoff Photo Shooting, 2019'
            ,'Bilstein MPP Process Team'
            ,'ITAM CDAS Projects Presentation'
            ,'Liverpool Purchasing Analytics Team'
        ]

        # Load images
        for idx in reversed(range(len(os.listdir(jpg_dir)))):
            jpg_file = f'{idx}.jpg'
            fig_ = Image.open(
                os.path.join(jpg_dir, jpg_file))
            
            st.image(fig_)
            st.caption(caption[idx])
