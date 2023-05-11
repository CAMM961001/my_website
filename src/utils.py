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


def render_button(url, name='View site', align='center'):
    button = f"""
            <div style="text-align: {align}"><p></p>
                <a href="{url}">
                    <button type="button" class="btn btn-outline-danger">
                        {name}
                    </button>
                </a>
            </div>
            """
    st.markdown(button, unsafe_allow_html=True)