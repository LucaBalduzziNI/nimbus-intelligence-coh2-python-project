import streamlit as st

# Session Keys
SESSION_IP = 'IP'
SESSION_COUNTRY_NAME = 'COUNTRY_NAME'
SESSION_COUNTRY_FLAG = 'COUNTRY_FLAG'
SESSION_COUNTRY_LANGUAGES = 'COUNTRY_LANGUAGES'
SESSION_PREF_LANG = 'PREF_LANG'
SESSION_PREF_LANG_SET = 'PREF_LANG_SET'
SESSION_INS_SOURCE_TEXT = 'INS_SOURCE_TEXT'
SESSION_INS_SOURCE_LANG = 'INS_SOURCE_LANG'
SESSION_INS_ERROR = 'INS_ERROR'
SESSION_TABLE_DEL = 'TABLE_DEL'

def _set_default(key: str, value: any = None):
    """Sets the default for the variable if not alredy set.

    Args:
        key (str): the session variable key
        value (any, optional): value of the session variable. Defaults to None.
    """
    if key not in st.session_state.keys():
        st.session_state.setdefault(key, value)

def initialize_session():
    """Initializes session variables.
    """
    _set_default(SESSION_IP)
    _set_default(SESSION_COUNTRY_NAME)
    _set_default(SESSION_COUNTRY_FLAG)
    _set_default(SESSION_COUNTRY_LANGUAGES)
    _set_default(SESSION_PREF_LANG)
    _set_default(SESSION_PREF_LANG_SET, False)
    _set_default(SESSION_INS_SOURCE_TEXT)
    _set_default(SESSION_INS_SOURCE_LANG)
    _set_default(SESSION_INS_ERROR)
    _set_default(SESSION_TABLE_DEL)