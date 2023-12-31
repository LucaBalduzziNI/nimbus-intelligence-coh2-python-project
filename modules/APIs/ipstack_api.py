# Modules
import requests

# Custom Modules
try:
    from .. import secret_stuff
    from ..errors import *
except Exception as e:
    import modules.secret_stuff
    from modules.errors import *


def resolve_ip(ip: str) -> dict:
    """Resolves the provided IP returning the code language spoken.

    Args:
        ip (str): IP address

    Raises:
        IpCantBeResolved: raised if given ip does not exist or it can't be resolved.
        ConnectionError: raised if the connection with the API was not successful

    Returns:
        dict: Dictionary containing the location code and a list of language codes spoken in this location
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
                language_list.append([language['code'], language['native']])
            country_code = data['country_code']
            country_name = data['country_name']
            country_flag = data['location']['country_flag']

            return {"country_code": country_code, "languages": language_list, "country_name": country_name, "country_flag": country_flag}
        else:
            raise IpCantBeResolved(ip)
    else:
        raise ConnectionError()

# Testing purposes
if __name__ == '__main__':
    ip = input('Inser IP address: ')
    print(resolve_ip(ip))       