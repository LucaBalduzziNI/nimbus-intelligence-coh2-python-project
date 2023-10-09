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

    st.markdown('### IP, country and language data')
    st.markdown('#### IPs per country')

    st.text("Total resolved IP addresses cached: "+str(ip_analytics()))
    st.bar_chart(country_code_analytics(), x = "COUNTRY_CODE")


    st.markdown('#### Preferred languages per country')
    countrySelect = st.selectbox("Country", country_list_analytics())
    st.bar_chart(country_language_analytics(countrySelect), x = "PREF_LANG_CODE")


if __name__ == '__main__':
    analytics()