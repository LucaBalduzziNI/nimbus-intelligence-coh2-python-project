# Modules
import streamlit as st
import pandas as pd

# Custom Modules
try:
    from ..gui.session import *
    from ..core_analytics import *
except Exception as e:
    from gui.session import *
    from core_analytics import *



def analytics():
  
    initialize_session()

    # Configurations
    st.set_page_config(page_title='Analytics', page_icon='📊', layout='wide')
        
    app_title = st.title('Analytics 📊')
        
    st.divider()
    
    st.bar_chart(ip_analytics)