import streamlit as st

# Session Keys
SESSION_IP = 'IP'
SESSION_COUNTRY_NAME = 'COUNTRY_NAME'
SESSION_COUNTRY_FLAG = 'COUNTRY_FLAG'
SESSION_COUNTRY_LANGUAGES = 'COUNTRY_LANGUAGES'
SESSION_PREF_LANG = 'PREF_LANG'
SESSION_PREF_LANG_SET = 'PREF_LANG_SET'

def _set_default(key: str, value: any = None):
    if key not in st.session_state.keys():
        st.session_state.setdefault(key, value)

def initialize_session():
    _set_default(SESSION_IP)
    _set_default(SESSION_COUNTRY_NAME)
    _set_default(SESSION_COUNTRY_FLAG)
    _set_default(SESSION_COUNTRY_LANGUAGES)
    _set_default(SESSION_PREF_LANG)
    _set_default(SESSION_PREF_LANG_SET, False)