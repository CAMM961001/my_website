import streamlit as st

import src.settings as setts
from src.portfolio import Portfolio
from src.about_me import AboutMe

from streamlit_option_menu import option_menu


# App settings
settings = setts.Settings()


# Site settings
st.set_page_config(
    page_title=settings.config['styling']['page_title'],
    layout=settings.config['styling']['layout'])


# --- SIDE BAR ---
with st.sidebar:
    
    # Professional summary
    st.write('Welcome\n')
    
    st.markdown('---')

    # Navigation menu
    st.write('Selecciona una página')

    selected = option_menu(
        menu_title=None,
        options=settings.config['styling']['pages'],
        icons=settings.config['styling']['menu_icons'],
        menu_icon='cast',
        default_index=0)
    
    st.markdown('---')


# --- PAGES: About Me ---
if selected == settings.config['styling']['pages'][0]:
    
    pages_ = AboutMe()

    st.title(pages_.page_title)

    st.markdown(pages_.descripcion)
        
    st.markdown('---')


# --- PAGES: Project portfolio ---
elif selected == settings.config['styling']['pages'][1]:
    
    pages_ = Portfolio()

    st.title(pages_.page_title)

    st.markdown(pages_.descripcion)
        
    st.markdown('---')


if __name__ == '__main__':
    settings.site_footer()