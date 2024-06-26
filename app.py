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
    page_title = settings.config['styling']['page_title']
    ,layout = settings.config['styling']['layout']
    ,initial_sidebar_state='expanded')


# --------------------------------------------------------------- SIDE BAR

# Side bar fixed width
st.markdown(
    body = '''
    <style>
        [data-testid="stSidebar"][aria-expanded="true"]{
            min-width: 325px;
            max-width: 325px;
        }'''
    ,unsafe_allow_html = True
)

with st.sidebar:
    # Initialize sidebar instance
    sb_ = SideBar()
    
    # Side bar title
    st.title(':sunglasses: ' + settings.config['styling']['page_title'])

    sb_.download_resume()

    # Navigation menu
    selected = option_menu(
        menu_title = None,
        options = settings.config['styling']['pages'],
        icons = settings.config['styling']['menu_icons'],
        menu_icon = 'cast',
        default_index = 0)
    
    sb_.profile_picture()

    # Profile description
    st.write('---')
    sb_.skills_picture()

    st.markdown(
        body=f'''
        <h1 style="text-align: center;">
            Lead Data Scientist at
            <br>
            <a href="https://mx.havas.com/" style="color: {settings.toml_config["theme"]["primaryColor"]}; text-decoration:none;">
            Havas Media Group</a>
        </h1>'''
        ,unsafe_allow_html=True)


# -------------------------------------------------------------- PORTFOLIO


if selected == settings.config['styling']['pages'][0]:
    
    pages_ = Portfolio()

    st.title(pages_.page_title)

    st.markdown('---')

    with st.container():
        col1, col2, col3 = st.columns(3, gap='medium')
        
        with col1:
            proj = 2
            pages_.render_project(
                name = pages_.data[proj]['name']
                ,contrib = pages_.data[proj]['contributors']
                ,desc = pages_.data[proj]['description']
                ,img_path = pages_.data[proj]['cover']
                ,site_url = pages_.data[proj]['site_url']
                ,src_url = pages_.data[proj]['src_url'])

        with col2:
            proj = 0
            pages_.render_project(
                name = pages_.data[proj]['name']
                ,contrib = pages_.data[proj]['contributors']
                ,desc = pages_.data[proj]['description']
                ,img_path = pages_.data[proj]['cover']
                ,site_url = pages_.data[proj]['site_url']
                ,src_url = pages_.data[proj]['src_url'])
        
        with col3:
            proj = 1
            pages_.render_project(
                name = pages_.data[proj]['name']
                ,contrib = pages_.data[proj]['contributors']
                ,desc = pages_.data[proj]['description']
                ,img_path = pages_.data[proj]['cover']
                ,site_url = pages_.data[proj]['site_url']
                ,src_url = pages_.data[proj]['src_url'])
            
    st.markdown('---')
    

# --------------------------------------------------------------- ABOUT ME


elif selected == settings.config['styling']['pages'][1]:
    
    pages_ = AboutMe()

    # Section titles
    st.title('About Me')

    # Section content
    st.markdown('---')
    col1, col2 = st.columns((3,1))
    with col1:
        st.header(':mantelpiece_clock: Professional Timeline')
        pages_.timeline()
        
        st.markdown('---')

        st.write(pages_.description[0], unsafe_allow_html=True)
    
    with col2:
        st.header('Galery')
        pages_.side_images()

    st.markdown('---')


if __name__ == '__main__':
    settings.site_footer()