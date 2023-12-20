import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from matplotlib import rcParams
from settings import Settings

# Figure text color specs
COLOR = 'black'
rcParams['text.color'] = COLOR
rcParams['axes.labelcolor'] = COLOR
rcParams['xtick.color'] = COLOR
rcParams['ytick.color'] = COLOR

# Load project settings
settings = Settings()

# Get todays date
today = pd.Timestamp.today().date()

# =======================================================================
# ============================ Timeline =================================
# =======================================================================

# Data preprocess for timeline visualization
df_ = (
    pd.read_csv(settings.config['path']['timeline'])
    .assign(
        nombre = lambda _df: _df.nombre.str.replace('\\n','\n')
        ,empresa = lambda _df: _df.empresa.str.replace('\\n','\n')
        ,inicio = lambda df_: pd.to_datetime(df_.inicio, format='%Y-%m-%d')
        ,fin = lambda df_: pd.to_datetime(df_.fin, format='%Y-%m-%d')
        ,ypos = lambda df_: df_.ypos.astype(int)
        ,delta = lambda df_: df_.delta.astype(int)))

# Figure specs
fig, ax = plt.subplots(figsize=(16,6))
ymin, ymax = df_.ypos.min() - 0.5, df_.ypos.max() + 0.5
covid_x = pd.to_datetime('20/03/2020', format='%d/%m/%Y')
professional = mpatches.Patch(color='#8acade', label='Professional')
education = mpatches.Patch(color='#c0e6bc', label='Education')
volunteer = mpatches.Patch(color='#eebbff', label='Volunteer')

# Covid pandemics reference line
ax.axvline(
    x=covid_x
    #,color=settings.config['images']['colors']['orange']
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
    #,color=settings.config['images']['colors']['orange']
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
        ,[df_.ypos[idx], df_.ypos[idx]]
        ,linewidth=6
        ,color=df_.color[idx])
    
    ax.scatter(
        x=[df_.inicio[idx], df_.fin[idx]]
        ,y=[df_.ypos[idx], df_.ypos[idx]]
        ,color=df_.color[idx]
        ,s=100)
    
    ax.text(
        x=df_.inicio[idx]
        ,y=df_.ypos[idx] + 0.35*df_.delta[idx]
        ,s=df_.nombre[idx]
        ,va='center')

# Figure annotations and styling
ax.set_ylim(bottom=ymin ,top=ymax)
ax.set_yticks(
    ticks=df_.ypos.unique()
    ,labels=df_.empresa.unique().astype(str))

ax.legend(
    loc='lower center'
    ,bbox_to_anchor=(0.5,-0.15)
    ,ncol=3, fancybox=True, handles=[professional, education, volunteer])

ax.grid(axis='y', alpha=0.25)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

fig.savefig('images/timeline.png', transparent=True, bbox_inches = 'tight')

if __name__ == '__main__':
    print('Job done')
