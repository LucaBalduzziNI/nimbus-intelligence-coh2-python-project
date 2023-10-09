# Modules
import streamlit as st

# Custom Modules
try:
    from ..gui.session import *
    from ..core_reset import reset_cache
except Exception as e:
    from gui.session import *
    from core_reset import reset_cache

def admin():
    initialize_session()

    # Configurations
    st.set_page_config(page_title='Admin', page_icon='🔒', layout='wide')
    
    app_title = st.title('Admin 🔒')
    
    st.divider()

    # Add new sentences
    st.markdown('### Add New Sentences')
    st.markdown('#### Write a sentence')
    sentence = st.text_input('A', label_visibility='hidden')
    st.markdown('#### Select a source language:')
    language = st.text_input('B', label_visibility='hidden')

    _, btn_insert_col, _ = st.columns((4,2,4))
    with btn_insert_col as col:
        st.button('Insert', use_container_width=True)
    st.divider()

    # Reset cache
    tables = ['Countries', 'IP_Addresses', 'Languages_Country', 'Languages', 'Translations']
    st.markdown('### Reset Cache')
    st.markdown('#### Choose a table to reset:')
    table = st.selectbox('A', tables, label_visibility='hidden')
    _, btn_col_delete, _ = st.columns((4,2,4))
    with btn_col_delete as col:
        st.button('Reset', on_click=reset_cache, use_container_width=True, args=(table,))

if __name__ == '__main__':
    admin()