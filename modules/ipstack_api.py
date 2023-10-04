# Modules
import requests

# Custom Modules
try:
    import secret_stuff
    from errors import *
except Exception as e:
    from . import secret_stuff
    from .errors import *


def resolve_ip(ip: str) -> str:
    """Resolves the provided IP returning the code language spoken.

    Args:
        ip (str): IP address

    Raises:
        IpCantBeResolved: _description_
        ConnectionError: _description_

    Returns:
        list: List of language codes (str) where the IP is
    """

    # IP Stack API Key
    API_KEY = secret_stuff.IP_STACK_API_KEY

    # Retrieve geolocation from IP stack
    response = requests.get(f"http://api.ipstack.com/{ip}?access_key={API_KEY}")
    
    # Check if HTTP request succeeded
    if response.status_code == 200:      
        data = response.json()
        language_list = []
        # Check if the Ip has been resolved
        if 'location' in data and data['location']['languages'] is not None:

            for language in data['location']['languages']:
                language_list.append(language['code'])

            return language_list
        else:
            raise IpCantBeResolved(ip)
    else:
        raise ConnectionError()

# Testing purposes
if __name__ == '__main__':
    ip = input('Inser IP address: ')
    print(resolve_ip(ip))       