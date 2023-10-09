# Modules
import streamlit as st

# Custom Modules
try:
    from ..gui.session import *
    from ..core_reset import reset_cache
    from ..core_set_pref_lang import set_pref_lang
except Exception as e:
    from gui.session import *
    from core_reset import reset_cache
    from core_set_pref_lang import set_pref_lang

def settings():
    initialize_session()

    # Configurations
    st.set_page_config(page_title='Settings', page_icon='⚙️', layout='wide')
    
    app_title = st.title('Settings ⚙️')
    
    st.divider()

    # Change prefered language if multiple are available
    if st.session_state[SESSION_COUNTRY_LANGUAGES] and len(st.session_state[SESSION_COUNTRY_LANGUAGES]) > 1:
        st.markdown('### Select your preferred language:')
        pref_lang_code = st.selectbox('', st.session_state[SESSION_COUNTRY_LANGUAGES], format_func=lambda language: language[1])
        st.session_state[SESSION_PREF_LANG] = pref_lang_code[0]
        _, btn_col_lang_sel, _ = st.columns((4,2,4))
        with btn_col_lang_sel as col:
            st.button('Confirm language', use_container_width=True, on_click=set_session_pref_lang, args=(st.session_state[SESSION_IP], st.session_state[SESSION_PREF_LANG]))

def set_session_pref_lang(ip_address: str, lang_code: str):
    st.session_state[SESSION_PREF_LANG_SET] = True
    set_pref_lang(ip_address, lang_code)

if __name__ == '__main__':
    settings()