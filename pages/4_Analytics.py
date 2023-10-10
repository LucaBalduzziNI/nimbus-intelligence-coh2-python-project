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
    st.bar_chart(country_code_analytics(), x = "COUNTRY_NAME")


    st.markdown('#### Preferred languages per country')
    country_list = country_list_analytics()
    print(country_list)
    countrySelect = st.selectbox("Country", country_list, format_func=lambda d: d['COUNTRY_NAME'])
    #st.bar_chart(country_language_analytics(countrySelect), x = "PREF_LANG_CODE")
    st.bar_chart(country_language_analytics(countrySelect['COUNTRY_CODE']), x = "PREF_LANG_CODE")

    st.markdown('### Translation data')
    st.text("Total cached sentence chunks for translation: "+str(chunk_analytics()))
    st.text("Total cached translations: "+str(translate_analytics()))

    st.markdown('#### Number of different translations per chunk')
    st.bar_chart(translate_chunk(), x = "TEXT_ID")


    st.markdown('#### Number of translated chunks per language')
    st.bar_chart(chunk_language(), x = "LANGUAGE_CODE")
    


if __name__ == '__main__':
    analytics()