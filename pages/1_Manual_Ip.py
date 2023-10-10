# Modules
import streamlit as st

# Custom Modules
from gui.session import *
from core_init import init_app

def manual_ip():
  
    initialize_session()

    # Configurations
    st.set_page_config(page_title='Manual Ip', page_icon='🌐', layout='wide')
    
    app_title = st.title('Manual Ip 🌐')
    
    st.divider()

    # List of ips for the demo
    ips = [None, '109.88.0.0', '67.139.45.218', '152.67.164.82', '131.227.153.30', '126.151.105.249', '187.238.122.202', '105.203.33.244', '179.138.100.251', '81.164.150.203']
    
    st.markdown('### Select an IP address from the list:')
    ip = st.selectbox('A', ips, label_visibility='hidden')
    _, btn_col, _ = st.columns((4,2,4))
    with btn_col as col:
        st.button('Confirm', on_click=set_ip, args=(ip,), use_container_width=True)

def set_ip(ip_address: str):
    """Sets the ip of the session and its session variables.

    Args:
        ip_address (str): the ip to set in the session
    """
    st.session_state[SESSION_IP] = ip_address
    # Setting the values only if the ip is valid
    if st.session_state[SESSION_IP]:  
        ip_country = init_app(userIP=st.session_state[SESSION_IP])
        if ip_country.pref_lang_code and ip_country.pref_lang_code != 'None':
            st.session_state[SESSION_PREF_LANG] = ip_country.pref_lang_code
            st.session_state[SESSION_PREF_LANG_SET] = True
        else:
            st.session_state[SESSION_PREF_LANG_SET] = False
        st.session_state[SESSION_COUNTRY_NAME] = ip_country.country_name
        st.session_state[SESSION_COUNTRY_FLAG] = ip_country.country_flag
        st.session_state[SESSION_COUNTRY_LANGUAGES] = ip_country.lang_details
    else:
        st.session_state[SESSION_PREF_LANG_SET] = False
        
if __name__ == '__main__':
    manual_ip()