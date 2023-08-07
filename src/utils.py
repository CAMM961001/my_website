import requests
import streamlit as st

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None    
    return r.json()


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def render_button(url, name='Visit site', align='center'):
    button = f'''
        <a href="{url}" style="text-decoration: none;">
            <div style="
                text-align: {align};
                padding: 0.5em 1em;
                color: #FFFFFF;
                background-color: #F63366;
                border-radius: 10px;">
                {name}
            </div>
        </a>
        '''
    st.markdown(button, unsafe_allow_html=True)