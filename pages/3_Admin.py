# Modules
import streamlit as st

# Custom Modules
try:
    from ..modules.errors import *
    from ..gui.session import *
    from ..core_reset import reset_cache
    from ..core_text_types import get_texts, add_text as _add_text
except Exception as e:
    from modules.errors import *
    from gui.session import *
    from core_reset import reset_cache
    from core_text_types import get_texts, add_text as _add_text

def admin():
    initialize_session()
    st.session_state[SESSION_INS_ERROR] = None

    # Configurations
    st.set_page_config(page_title='Admin', page_icon='🔒', layout='wide')
    
    app_title = st.title('Admin 🔒')
    
    st.divider()

    # Add new sentences
    st.markdown('### Add New Sentences')
    if st.session_state[SESSION_INS_ERROR]:
        st.error(st.session_state[SESSION_INS_ERROR])

    input_col, display_sentences_col = st.columns(2)
    with input_col as col:
        st.markdown('#### Write a sentence')
        st.text_input('A', label_visibility='hidden', key=SESSION_INS_SOURCE_TEXT)
        st.markdown('#### Select a source language:')
        st.text_input('B', label_visibility='hidden', key=SESSION_INS_SOURCE_LANG)

    with display_sentences_col as col:
        st.markdown('#### Cached Sentences')
        st.dataframe(get_texts(), use_container_width=True)

    _, btn_insert_col, _ = st.columns((4,2,4))
    with btn_insert_col as col:
        # The button gets activated once the input is correct
        disabled = not check_input()
        st.button('Insert', use_container_width=True, on_click=add_text, args=(st.session_state[SESSION_INS_SOURCE_TEXT], st.session_state[SESSION_INS_SOURCE_LANG]), disabled=disabled)

    st.divider()

    # Reset cache
    tables = ['Countries', 'IP_Addresses', 'Languages_Country', 'Languages', 'Translations', 'Text_Types']
    st.markdown('### Reset Cache')
    st.markdown('#### Choose a table to reset:')
    st.selectbox('A', tables, key=SESSION_TABLE_DEL, label_visibility='hidden')
    _, btn_col_delete, _ = st.columns((4,2,4))
    with btn_col_delete as col:
        st.button('Reset', on_click=reset_cache, use_container_width=True, args=(st.session_state[SESSION_TABLE_DEL],))

def check_input() -> bool:
    """Checks the input fields returning True if the are not None and contain text.

    Returns:
        bool: the evaluation of the check
    """
    return (st.session_state[SESSION_INS_SOURCE_TEXT] is not None 
            and st.session_state[SESSION_INS_SOURCE_TEXT] != ''
            and st.session_state[SESSION_INS_SOURCE_LANG] is not None
            and st.session_state[SESSION_INS_SOURCE_LANG] != '')

def add_text(text: str, source_lang: str):
    """Adds a new text_type in the DB and resets session values of input.

    Args:
        text (str): the text_type to be stored
        source_lang (str): the source language of the text
    """
    try:
        _add_text(text, source_lang)
        st.session_state[SESSION_INS_ERROR] = None
        st.session_state[SESSION_INS_SOURCE_TEXT] = None
        st.session_state[SESSION_INS_SOURCE_TEXT] = None
    except TextTypeIsAlreadyStored as e:
        st.session_state[SESSION_INS_ERROR] = str(e)

if __name__ == '__main__':
    admin()