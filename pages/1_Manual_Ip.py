# Modules
import time
import base64
import streamlit as st
from streamlit_extras import add_vertical_space, stateful_button

# Custom Modules
from modules import ipify_api, ipstack_api, tts_api
from gui.session import *
from core_init import init_app

def manual_ip():
  
    initialize_session()

    # Configurations
    st.set_page_config(page_title='Manual Ip', page_icon='🌐', layout='wide')
    
    app_title = st.title('Manual Ip 🌐')
    
    st.divider()

    ips = [None, '109.88.0.0']
    ip = st.selectbox('Select an Ip', ips)
    if ip:
        st.session_state[SESSION_IP] = ip
    st.button('Confirm', on_click=set_ip)

def set_ip():
    ip_country = init_app(userIP=st.session_state[SESSION_IP])
    #st.session_state[SESSION_IP] = ip_country.ip_address
    if ip_country.pref_lang_code:
        st.session_state[SESSION_PREF_LANG] = ip_country.pref_lang_code
        st.session_state[SESSION_PREF_LANG_SET] = False
    st.session_state[SESSION_COUNTRY_NAME] = ip_country.country_name
    st.session_state[SESSION_COUNTRY_FLAG] = ip_country.country_flag
    st.session_state[SESSION_COUNTRY_LANGUAGES] = ip_country.lang_details

if __name__ == '__main__':
    manual_ip()