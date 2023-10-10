# Modules
import streamlit as st

# Custom Modules
try:
    from ..gui.session import *
    from ..core_set_pref_lang import set_pref_lang
except Exception as e:
    from gui.session import *
    from core_set_pref_lang import set_pref_lang

def settings():
    initialize_session()

    # Configurations
    st.set_page_config(page_title='Settings', page_icon='⚙️', layout='wide')
    
    app_title = st.title('Settings ⚙️')
    
    st.divider()

    # Change prefered language if multiple are available
    if st.session_state[SESSION_COUNTRY_LANGUAGES] and len(st.session_state[SESSION_COUNTRY_LANGUAGES]) > 1:

        index = 0
        # Indexing the selected language
        if st.session_state[SESSION_PREF_LANG_SET]:
            index = list(map(lambda l: l[0], st.session_state[SESSION_COUNTRY_LANGUAGES])).index(st.session_state[SESSION_PREF_LANG])
        
        st.markdown('### Select your preferred language:')
        pref_lang = st.selectbox('A', st.session_state[SESSION_COUNTRY_LANGUAGES], format_func=lambda language: language[1], index=index, label_visibility='hidden')
        
        # Assigning the pref_lang_code
        _, btn_col_lang_sel, _ = st.columns((4,2,4))
        with btn_col_lang_sel as col:
            st.button('Confirm language', use_container_width=True, on_click=set_session_pref_lang, args=(st.session_state[SESSION_IP], pref_lang[0]))
        
        st.divider()

def set_session_pref_lang(ip_address: str, pref_lang_code: str):
    """Sets the preferred language for the session, as a session variable and in the DB.

    Args:
        ip_address (str): ip address to make the changes on
        pref_lang_code (str): language code to be set as preferred
    """
    st.session_state[SESSION_PREF_LANG_SET] = True
    st.session_state[SESSION_PREF_LANG] = pref_lang_code
    set_pref_lang(ip_address, pref_lang_code)

if __name__ == '__main__':
    settings()