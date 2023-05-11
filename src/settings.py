'''
Module to store project settings class
'''

import os
import yaml

from streamlit import markdown
from datetime import datetime


class Settings():
    def __init__(self):
        self.ROOT = os.path.dirname(os.path.dirname(__file__))
        self.TODAY = datetime.now()
        
        with open(os.path.join(self.ROOT, 'config.yml'), 'r') as file:
            self.config = yaml.safe_load(file)
        file.close


    def __str__(self):
        prompt = f"CONFIG:\t{self.config}\n"
        return prompt
    

    def site_footer(self):
        footer = f'''
        <p style="text-align: center; font-size: 15px">
            <br>
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-c-circle" viewBox="0 0 16 16">
                    <path d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8Zm15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0ZM8.146 4.992c-1.212 0-1.927.92-1.927 2.502v1.06c0 1.571.703 2.462 1.927 2.462.979 0 1.641-.586 1.729-1.418h1.295v.093c-.1 1.448-1.354 2.467-3.03 2.467-2.091 0-3.269-1.336-3.269-3.603V7.482c0-2.261 1.201-3.638 3.27-3.638 1.681 0 2.935 1.054 3.029 2.572v.088H9.875c-.088-.879-.768-1.512-1.729-1.512Z"/>
                </svg> Miguel Castaneda 2023</br>
                Built with <a href={self.config['main']['components_repository']} style="color: #F63366; text-decoration:none;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-git" viewBox="0 0 16 16">
                        <path d="M15.698 7.287 8.712.302a1.03 1.03 0 0 0-1.457 0l-1.45 1.45 1.84 1.84a1.223 1.223 0 0 1 1.55 1.56l1.773 1.774a1.224 1.224 0 0 1 1.267 2.025 1.226 1.226 0 0 1-2.002-1.334L8.58 5.963v4.353a1.226 1.226 0 1 1-1.008-.036V5.887a1.226 1.226 0 0 1-.666-1.608L5.093 2.465l-4.79 4.79a1.03 1.03 0 0 0 0 1.457l6.986 6.986a1.03 1.03 0 0 0 1.457 0l6.953-6.953a1.031 1.031 0 0 0 0-1.457"/>
                    </svg>
                </a> and <a href={self.config['main']['streamlit']} style="color: #F63366; text-decoration:none;">
                    Streamlit
                </a>
            </br>
        </p>'''

        markdown(footer, unsafe_allow_html=True)


if __name__ == '__main__':
    settings = Settings()
    print(str(settings))