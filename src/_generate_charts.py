import json
import pandas as pd
import matplotlib.pyplot as plt
import settings as setts

from matplotlib import rcParams

# Figure text color specs
COLOR = 'black'
rcParams['text.color'] = COLOR
rcParams['axes.labelcolor'] = COLOR
rcParams['xtick.color'] = COLOR
rcParams['ytick.color'] = COLOR

# Load project settings
settings = setts.Settings()

# Get todays date
today = pd.Timestamp.today().date()

# =======================================================================
# ============================ Timeline =================================
# =======================================================================

# Open timeline asset file
with open(settings.config['path']['timeline'], 'r') as file:
    df_ = json.load(file)
file.close()

# Data preprocess for timeline visualization
df_ = (
    pd.DataFrame(df_)
    .assign(
        inicio = lambda df_: pd.to_datetime(df_.inicio, format='%d/%m/%Y')
        ,fin = lambda df_: pd.to_datetime(df_.fin, format='%d/%m/%Y')
        ,clase = lambda df_: df_.clase.astype(int)
        ,delta = lambda df_: df_.delta.astype(int)))

# Figure specs
fig, ax = plt.subplots(figsize=(16,6))
ymin, ymax = df_.clase.min() - 0.5, df_.clase.max() + 0.5
covid_x = pd.to_datetime('20/03/2020', format='%d/%m/%Y')

# Covid pandemics reference line
ax.axvline(
    x=covid_x
    ,color=settings.config['images']['colors']['orange']
    ,alpha=0.4)

# Covid pandemics annotation
ax.text(
    x=covid_x
    ,y=ymin + 0.3
    ,s=' Coronavirus isolation\n is declared in Mexico'
    ,alpha=0.4)

# Today reference line
ax.axvline(
    x=today
    ,color=settings.config['images']['colors']['orange']
    ,alpha=0.4)

# Today annotation
ax.text(
    x=today
    ,y=1.3
    ,s=' The best is\n yet to come...'
    ,alpha=0.4)

for idx in range(df_.shape[0]):
    # Gráficas
    ax.plot(
        [df_.inicio[idx], df_.fin[idx]]
        ,[df_.clase[idx], df_.clase[idx]]
        ,linewidth=6
        ,color=df_.color[idx])
    
    ax.scatter(
        x=[df_.inicio[idx], df_.fin[idx]]
        ,y=[df_.clase[idx], df_.clase[idx]]
        ,color=df_.color[idx]
        ,s=100)
    
    ax.text(
        x=df_.inicio[idx]
        ,y=df_.clase[idx] + 0.35*df_.delta[idx]
        ,s=df_.nombre[idx]
        ,va='center')

# Figure annotations and styling
ax.set_ylim(bottom=ymin ,top=ymax)
ax.set_yticks(
    ticks=df_.clase.unique()
    ,labels=df_.empresa.unique())

ax.grid(axis='y', alpha=0.25)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

fig.savefig('images/timeline.png', transparent=True, bbox_inches = 'tight')


# =======================================================================
# ============================ TechStack ================================
# =======================================================================

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

# Advanced analytics
fig = plt.figure()
ax = fig.add_subplot()

ax.barh(
    y=analytics
    ,width=[4,4,5,5,4,3,2]
    ,color=settings.config['images']['colors']['green'])

ax.set_title('Advanced Analytics', fontsize=18)
ax.set_xticks(
    ticks=list(skill_level.keys())
    ,labels=list(skill_level.values()))
ax.set_xlim(right=max(skill_level.keys()))
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

#fig.savefig('images/analytics.png', transparent=True, bbox_inches = 'tight')

# Development
fig = plt.figure()
ax = fig.add_subplot()

ax.barh(
    y=devs
    ,width=[1,4,2,5]
    ,color=settings.config['images']['colors']['orange'])

ax.set_title('Development', fontsize=18)
ax.set_xticks(
    ticks=list(skill_level.keys())
    ,labels=list(skill_level.values()))
ax.set_xlim(right=max(skill_level.keys()))
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

#fig.savefig('images/development.png', transparent=True, bbox_inches = 'tight')

# Business Inteligence
fig = plt.figure()
ax = fig.add_subplot()

ax.barh(
    y=bi
    ,width=[5,3,2,5]
    ,color=settings.config['images']['colors']['blue'])

ax.set_title('Business Inteligence', fontsize=18)
ax.set_xticks(
    ticks=list(skill_level.keys())
    ,labels=list(skill_level.values()))
ax.set_xlim(right=max(skill_level.keys()))
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

#fig.savefig('images/bi.png', transparent=True, bbox_inches = 'tight')

# Cloud
fig = plt.figure()
ax = fig.add_subplot()

ax.barh(
    y=storage
    ,width=[4,4,3,1]
    ,color=settings.config['images']['colors']['pink'])

ax.set_title('Data Processing & Storage', fontsize=18)
ax.set_xticks(
    ticks=list(skill_level.keys())
    ,labels=list(skill_level.values()))
ax.set_xlim(right=max(skill_level.keys()))
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

#fig.savefig('images/cloud.png', transparent=True, bbox_inches = 'tight')


if __name__ == '__main__':
    print('Job done')
