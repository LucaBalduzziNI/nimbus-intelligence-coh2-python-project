import streamlit as st
import time

# Session Keys
SESSION_IP = 'IP'
SESSION_LOADING_IP = 'LOADING_IP'
SESSION_COUNTRY_NAME = 'COUNTRY_NAME'
SESSION_COUNTRY_FLAG = 'COUNTRY_FLAG'
SESSION_COUNTRY_LANGUAGES = 'COUNTRY_LANGUAGES'
SESSION_PREF_LANG = 'PREF_LANG'
SESSION_PREF_LANG_SET = 'PREF_LANG_SET'
SESSION_AUDIO_AUTOPLAY = 'AUDIO_AUTOPLAY'

st.session_state.setdefault(SESSION_IP, '')
st.session_state.setdefault(SESSION_LOADING_IP, '')
st.session_state.setdefault(SESSION_PREF_LANG, '')
st.session_state.setdefault(SESSION_PREF_LANG_SET, False)
st.session_state.setdefault(SESSION_AUDIO_AUTOPLAY, True)

time.sleep(1)