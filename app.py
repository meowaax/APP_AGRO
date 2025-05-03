import streamlit as st
from controlers.config import show_title, set_page_configuration
set_page_configuration()
from pags.CRUD_danos import main as main_danos
from pags.home import main as main_home
from pags.download import main as main_download
from controlers.sidebar import streamlit_menu, sidebar_content

show_title()
selected_option = streamlit_menu()


if selected_option == 'Home':
    main_home()

elif selected_option == 'Registros':
    main_danos()

elif selected_option == 'Download':
    main_download()

sidebar_content()
