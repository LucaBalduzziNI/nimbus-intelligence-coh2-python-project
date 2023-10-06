# Modules
import time
import base64
import streamlit as st
from streamlit_extras import add_vertical_space, stateful_button

# Custom Modules
from modules import ipify_api, ipstack_api, tts_api
from gui_utils.session import *



# App
def main():

    # Configurations
    st.set_page_config(page_title='Translation and TTS App', page_icon='🌐', layout='wide')
    
    # Session Settings
    st.session_state.setdefault(SESSION_IP, '')
    st.session_state.setdefault(SESSION_LOADING_IP, '')
    st.session_state.setdefault(SESSION_PREF_LANG, '')
    st.session_state.setdefault(SESSION_PREF_LANG_SET, False)
    st.session_state.setdefault(SESSION_AUDIO_AUTOPLAY, True)
    
    app_title = st.title('Translation and TTS App 🌐')
    
    st.divider()
    
    if st.session_state[SESSION_IP] == '':
        # Start geolocalization
        _, btn_col, _ = st.columns((4,2,4))
        with btn_col as col:
            st.button('Click for Geolocalization!', on_click=get_ip, use_container_width=True)

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
        languages = ['en', 'it']
        #set_pref_lang('it')
        play = False
        if st.session_state[SESSION_PREF_LANG] == '' and len(languages) > 1 and st.session_state[SESSION_PREF_LANG_SET] == False:
            preferred_lang = st.selectbox('Select your preferred language', languages, key=SESSION_PREF_LANG)
            _, btn_col_lang_sel, _ = st.columns(3)
            with btn_col_lang_sel as col:
                stateful_button.button('Confirm language', key=SESSION_PREF_LANG_SET, on_click=lambda: set_pref_lang(preferred_lang),  use_container_width=True)
                #st.button('Confirm language', key=SESSION_PREF_LANG_SET, on_click=lambda: set_pref_lang(preferred_lang),  use_container_width=True)
        else:
            st.session_state[SESSION_PREF_LANG_SET] = True
        
        # Greet the user
        greeting = 'Buongiorno'
        audio = tts_api.text_to_speech(greeting, st.session_state[SESSION_PREF_LANG])
        md_audio = md_autoplay_audio(audio)
        if st.session_state[SESSION_PREF_LANG_SET]:
            text_col, audio_col = st.columns(2)
            with text_col as col:
                st.text(greeting)
            
            with audio_col as col:
                st.markdown(md_audio, unsafe_allow_html=True)

                
def get_ip():
    st.session_state[SESSION_IP] = ipify_api.get_ip()
    geoloc = ipstack_api.resolve_ip(st.session_state[SESSION_IP])
    st.session_state[SESSION_COUNTRY_NAME] = geoloc['country_name']
    st.session_state[SESSION_COUNTRY_FLAG] = geoloc['country_flag']

def set_pref_lang(language: str):
    st.session_state[SESSION_PREF_LANG] = language

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