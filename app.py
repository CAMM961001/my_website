import streamlit as st

from streamlit_option_menu import option_menu

from src.settings import Settings
from src.side_bar import SideBar
from src.about_me import AboutMe
from src.portfolio import Portfolio


# App settings
settings = Settings()

# Site settings
st.set_page_config(
    page_title=settings.config['styling']['page_title'],
    layout=settings.config['styling']['layout'])


# --- SIDE BAR ---
with st.sidebar:
    
    # Initialize sidebar instance
    sb_ = SideBar()
    
    # Side bar title
    st.title(':sunglasses: '+settings.config['styling']['page_title'])

    sb_.download_resume()

    # Navigation menu
    selected = option_menu(
        menu_title=None,
        options=settings.config['styling']['pages'],
        icons=settings.config['styling']['menu_icons'],
        menu_icon='cast',
        default_index=0)
    
    sb_.profile_picture()

    sb_.social_media_buttons()


# --- PAGES: About Me ---
if selected == settings.config['styling']['pages'][0]:
    
    pages_ = AboutMe()

    # Page title
    st.title(':wave: About Me')
    # Section content
    col1, col2 = st.columns((3,1))
    with col1:
        st.write(pages_.description[0], unsafe_allow_html=True)
    
    with col2:
        pages_.side_images()

    # Section header
    st.header(':mantelpiece_clock: Timeline')
    pages_.timeline()

    # Section header
    st.header(':space_invader: Technology Stack')
    pages_.skills()
        
    st.markdown('---')


# --- PAGES: Project portfolio ---
elif selected == settings.config['styling']['pages'][1]:
    
    pages_ = Portfolio()

    st.title(pages_.page_title)

    pages_.first_row()
        
    st.markdown('---')


if __name__ == '__main__':
    settings.site_footer()