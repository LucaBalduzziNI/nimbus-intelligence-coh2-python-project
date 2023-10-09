# Modules
import time
import base64
import streamlit as st
from streamlit_extras import add_vertical_space, stateful_button

# Custom Modules
from modules import ipify_api, ipstack_api, tts_api
from gui.session import *
from core_init import init_app

# App
def main():

    initialize_session()
    
    # Configurations
    st.set_page_config(page_title='Translation and TTS App', page_icon='🌐', layout='wide')
    
    app_title = st.title('Translation and TTS App 🌐')
    
    st.divider()
    
    if not st.session_state[SESSION_IP]:
        # Start geolocalization
        _, btn_col, _ = st.columns((4,2,4))
        with btn_col as col:
            st.button('Click for Geolocalization!', on_click=init_ip, use_container_width=True)
    else:
        # Displaying ip infos and country flag
        ip_col, flag_col = st.columns(2)
        with ip_col as col:
            add_vertical_space.add_vertical_space(3)
            st.text(f'Your IP is {st.session_state[SESSION_IP]} located in {st.session_state[SESSION_COUNTRY_NAME]}.')
            add_vertical_space.add_vertical_space(2)
        with flag_col as col:
            add_vertical_space.add_vertical_space(1)
            st.image(st.session_state[SESSION_COUNTRY_FLAG], width=100)
        st.divider()
        
        # Checking if multiple languages can be selected or aready selected preferred language
        if not st.session_state[SESSION_PREF_LANG_SET]:
            st.selectbox('Select your preferred language', map(lambda i: i[0], st.session_state[SESSION_COUNTRY_LANGUAGES]), key=SESSION_PREF_LANG)
            _, btn_col_lang_sel, _ = st.columns(3)
            with btn_col_lang_sel as col:
                st.button('Confirm language', on_click=pref_lang_set, use_container_width=True)
        else:
            # Greet the user
            greeting = 'Good Morning'
            audio = tts_api.text_to_speech(greeting, st.session_state[SESSION_PREF_LANG])
            md_audio = md_autoplay_audio(audio)
            text_col, audio_col = st.columns(2)
            with text_col as col:
                st.text(greeting)
            with audio_col as col:
                st.markdown(md_audio, unsafe_allow_html=True)
                
def init_ip():
    ip_country = init_app()
    st.session_state[SESSION_IP] = ip_country.ip_address
    if ip_country.pref_lang_code:
        st.session_state[SESSION_PREF_LANG] = ip_country.pref_lang_code
        st.session_state[SESSION_PREF_LANG_SET] = True
    st.session_state[SESSION_COUNTRY_NAME] = ip_country.country_name
    st.session_state[SESSION_COUNTRY_FLAG] = ip_country.country_flag
    st.session_state[SESSION_COUNTRY_LANGUAGES] = ip_country.lang_details

def pref_lang_set():
    st.session_state[SESSION_PREF_LANG_SET] = True

def md_autoplay_audio(audio: bytes) -> str:
    b64 = base64.b64encode(audio).decode()
    md = f"""
        <audio controls autoplay="true">
        <source src="data:audio/wav;base64,{b64}" type="audio/wav">
        </audio>
    """
    return md

if __name__ == '__main__':
    main()
