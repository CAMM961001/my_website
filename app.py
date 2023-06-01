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
    
    pages_ = Portfolio()

    st.title(pages_.page_title)

    with st.container():
        col1, col2, col3 = st.columns(3, gap='large')
        
        with col1:
            proj = 0
            pages_.render_project(
                name=pages_.data[proj]['name']
                ,contrib=pages_.data[proj]['contributors']
                ,desc=pages_.data[proj]['description']
                ,img_path=pages_.data[proj]['cover']
                ,site_url=pages_.data[proj]['site_url']
                ,src_url=pages_.data[proj]['src_url'])
        
        with col2:
            proj = 1
            pages_.render_project(
                name=pages_.data[proj]['name']
                ,contrib=pages_.data[proj]['contributors']
                ,desc=pages_.data[proj]['description']
                ,img_path=pages_.data[proj]['cover']
                ,site_url=pages_.data[proj]['site_url']
                ,src_url=pages_.data[proj]['src_url'])
            
    st.markdown('---')
    

elif selected == settings.config['styling']['pages'][1]:
    
    pages_ = AboutMe()

    # Page title
    st.title(':wave: About Me')
    # Section content
    col1, col2 = st.columns((3,1))
    with col1:
        st.write(pages_.description[0], unsafe_allow_html=True)
        
        # Section header
        st.header(':mantelpiece_clock: My resumen in a timeline')
        pages_.timeline()
    
    with col2:
        pages_.side_images()


if __name__ == '__main__':
    settings.site_footer()