# Modules
import requests

# Custom Modules
try:
    from errors import *
except Exception as e:
    from .errors import *

def get_ip() -> str:
    """Gets the IP of the machine.

    Returns:
        str: IP address
    """
    return(requests.get('https://api.ipify.org').text)