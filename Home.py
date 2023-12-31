# Modules
import base64
import streamlit as st
from streamlit_extras import add_vertical_space

# Custom Modules
try:
    from gui.session import *
    from modules.core.core_init import init_app
    from modules.core.core_set_pref_lang import set_pref_lang
    from modules.core.core_info import get_info
except Exception as e:
    raise e

# App
def home():

    initialize_session()
    
    # Configurations
    st.set_page_config(page_title='SkySpeak', page_icon='🌐', layout='wide')
    
    app_title = st.title('SkySpeak 🌐')
    
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
            st.markdown(f'#### Your IP is {st.session_state[SESSION_IP]} located in {st.session_state[SESSION_COUNTRY_NAME]}.')
            add_vertical_space.add_vertical_space(2)
        with flag_col as col:
            add_vertical_space.add_vertical_space(1)
            st.image(st.session_state[SESSION_COUNTRY_FLAG], width=100)
        st.divider()
        
        # Checking if multiple languages can be selected or aready selected preferred language
        if not st.session_state[SESSION_PREF_LANG_SET]:
            st.markdown('### Select your preferred language:')
            pref_lang = st.selectbox('A', st.session_state[SESSION_COUNTRY_LANGUAGES], format_func=lambda language: language[1], label_visibility='hidden')
            _, btn_col_lang_sel, _ = st.columns(3)
            with btn_col_lang_sel as col:
                st.button('Confirm language', use_container_width=True, on_click=set_session_pref_lang, args=(st.session_state[SESSION_IP], pref_lang[0]))
        else:
            # Greet the user with info about weather
            info = get_info(st.session_state[SESSION_IP], st.session_state[SESSION_PREF_LANG])
            md_audio = md_autoplay_audio(info[1])
            text_col, audio_col = st.columns(2)
            with text_col as col:
                st.write(info[0])
            with audio_col as col:
                st.markdown(md_audio, unsafe_allow_html=True)
                
def init_ip():
    """Inits the ip and sets the session variables
    """
    ip_country = init_app()
    st.session_state[SESSION_IP] = ip_country.ip_address
    if ip_country.pref_lang_code:
        st.session_state[SESSION_PREF_LANG] = ip_country.pref_lang_code
        st.session_state[SESSION_PREF_LANG_SET] = True
    st.session_state[SESSION_COUNTRY_NAME] = ip_country.country_name
    st.session_state[SESSION_COUNTRY_FLAG] = ip_country.country_flag
    st.session_state[SESSION_COUNTRY_LANGUAGES] = ip_country.lang_details

def set_session_pref_lang(ip_address: str, pref_lang_code: str):
    """Sets the preferred language for the session, as a session variable and in the DB.

    Args:
        ip_address (str): ip address to make the changes on
        pref_lang_code (str): language code to be set as preferred
    """
    st.session_state[SESSION_PREF_LANG_SET] = True
    st.session_state[SESSION_PREF_LANG] = pref_lang_code
    set_pref_lang(ip_address, pref_lang_code)

def md_autoplay_audio(audio: bytes) -> str:
    """Creates a md text to incorporate the audio in the app. Makes it auto start.

    Args:
        audio (bytes): the audio to be embedded in the markdown
    """
    b64 = base64.b64encode(audio).decode()
    md = f"""
        <audio controls autoplay="true">
        <source src="data:audio/wav;base64,{b64}" type="audio/wav">
        </audio>
    """
    return md

if __name__ == '__main__':
    home()
