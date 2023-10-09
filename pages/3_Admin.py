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

    # Reset cache
    st.markdown('### Reset Cache')
    _, btn_col_delete, _ = st.columns((4,2,4))
    with btn_col_delete as col:
        st.button('Reset', on_click=reset_cache, use_container_width=True)

if __name__ == '__main__':
    admin()