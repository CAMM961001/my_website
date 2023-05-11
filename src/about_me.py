import json
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

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

        # Open timeline asset file
        with open(settings.config['path']['timeline'], 'r') as file:
            data = json.load(file)
        file.close()

        # Data preprocess for visualization
        data = (
            pd.DataFrame(data)
            .assign(
                inicio = lambda df_: pd.to_datetime(df_.inicio, format='%d/%m/%Y')
                ,fin = lambda df_: pd.to_datetime(df_.fin, format='%d/%m/%Y')
                ,clase = lambda df_: df_.clase.astype(int)
                ,delta = lambda df_: df_.delta.astype(int)))
        
        # Figure specs
        fig, ax = plt.subplots(figsize=(16,6))
        ymin, ymax = data.clase.min() - 0.5, data.clase.max() + 0.5
        covid_x = pd.to_datetime('20/03/2020', format='%d/%m/%Y')
        
        # Covid pandemics reference line
        ax.axvline(
            x=covid_x
            ,color='red',
            alpha=0.4)
        
        # Covid pandemics annotation
        ax.text(
            x=covid_x
            ,y=ymin + 0.3
            ,s=' Coronavirus isolation\n is declared in Mexico',
            alpha=0.4)

        # Today reference line
        ax.axvline(
            x=self.today
            ,color='red',
            alpha=0.4)

        # Today annotation
        ax.text(
            x=self.today
            ,y=1.3
            ,s=' The best is\n yet to come...',
            alpha=0.4)

        for idx in range(data.shape[0]):
            # Gráficas
            ax.plot(
                [data.inicio[idx], data.fin[idx]]
                ,[data.clase[idx], data.clase[idx]]
                ,linewidth=6
                ,color=data.color[idx])
            
            ax.scatter(
                x=[data.inicio[idx], data.fin[idx]]
                ,y=[data.clase[idx], data.clase[idx]]
                ,color=data.color[idx]
                ,s=100)
            
            ax.text(
                x=data.inicio[idx]
                ,y=data.clase[idx] + 0.35*data.delta[idx]
                ,s=data.nombre[idx]
                ,va='center')

        # Figure annotations and styling
        ax.set_ylim(bottom=ymin ,top=ymax)
        ax.set_yticks(
            ticks=data.clase.unique()
            ,labels=data.empresa.unique())
        
        ax.grid(axis='y', alpha=0.25)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)

        # Render streamlit object
        st.pyplot(fig=fig, clear_figure=True)


    def skills(self):
        # Section header
        st.header('Technology Stack')

        # Section description
        st.write(self.description[2], unsafe_allow_html=True)

        skill_level = {
                    1:'Recruit'
                    ,2:'Regular'
                    ,3:'Hardened'
                    ,4:'Veteran'
                    ,5:'Legend'}
        
        analytics = ['Numpy','Scipy','Pandas','Matplotlib','ScikitLearn','TensorFlow','Tidyverse']
        devs = ['Flask','SQL Connectors','Docker','Git-GitHub']
        bi = ['Excel','Excel VBA','R Shiny', 'Streamlit']
        storage = ['Postgres','SQLServer','SQLite', 'Bash']
        
        with st.container():
            col1, col2 = st.columns((1,1))

            with col1:
                fig = plt.figure()
                ax = fig.add_subplot()

                ax.barh(
                    y=analytics
                    ,width=[4,4,5,5,4,3,2]
                    ,color='green'
                    ,alpha=0.5)

                ax.set_title('Advanced Analytics', fontsize=18)
                ax.set_xticks(
                    ticks=list(skill_level.keys())
                    ,labels=list(skill_level.values()))
                ax.set_xlim(right=max(skill_level.keys()))
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)
                ax.spines['left'].set_visible(False)
                
                #Add plot to streamlit
                st.pyplot(
                    fig=fig
                    ,clear_figure=True)
            
            with col2:
                fig = plt.figure()
                ax = fig.add_subplot()

                ax.barh(
                    y=devs
                    ,width=[1,4,2,5]
                    ,color='red'
                    ,alpha=0.5)

                ax.set_title('Development', fontsize=18)
                ax.set_xticks(
                    ticks=list(skill_level.keys())
                    ,labels=list(skill_level.values()))
                ax.set_xlim(right=max(skill_level.keys()))
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)
                ax.spines['left'].set_visible(False)

                #Add plot to streamlit
                st.pyplot(
                    fig=fig
                    ,clear_figure=True)
        

        with st.container():
            col1, col2 = st.columns((1,1))

            with col1:
                fig = plt.figure()
                ax = fig.add_subplot()

                ax.barh(
                    y=bi
                    ,width=[5,3,2,5]
                    ,color='blue'
                    ,alpha=0.5)

                ax.set_title('Bussines Inteligence', fontsize=18)
                ax.set_xticks(
                    ticks=list(skill_level.keys())
                    ,labels=list(skill_level.values()))
                ax.set_xlim(right=max(skill_level.keys()))
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)
                ax.spines['left'].set_visible(False)
                
                #Add plot to streamlit
                st.pyplot(
                    fig=fig
                    ,clear_figure=True)
            
            with col2:
                fig = plt.figure()
                ax = fig.add_subplot()

                ax.barh(
                    y=storage
                    ,width=[4,4,3,1]
                    ,color='purple'
                    ,alpha=0.5)

                ax.set_title('Data Processing & Storage', fontsize=18)
                ax.set_xticks(
                    ticks=list(skill_level.keys())
                    ,labels=list(skill_level.values()))
                ax.set_xlim(right=max(skill_level.keys()))
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)
                ax.spines['left'].set_visible(False)

                #Add plot to streamlit
                st.pyplot(
                    fig=fig
                    ,clear_figure=True)
        
        st.write("###")
