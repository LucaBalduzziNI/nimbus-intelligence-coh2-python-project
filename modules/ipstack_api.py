# Modules
import requests

# Custom Modules
import secret_stuff
from errors import *


def resolve_ip(ip: str):
    # IP Stack API Key
    API_KEY = secret_stuff.IP_STACK_API_KEY

    # Retrieve geolocation from IP stack
    response = requests.get(f"http://api.ipstack.com/{ip}?access_key={API_KEY}")
    
    # Check if HTTP request succeeded
    if response.status_code == 200:      
        data = response.json()

        # Check if the Ip has been resolved
        if 'location' in data:
            return data['location']['languages'][0]['name']
        else:
            raise IpCantBeResolved(ip) 
    else:
        raise ConnectionError()

# Testing purposes
if __name__ == '__main__':
    address = input('Inser IP address: ')
    print(resolve_ip(address))
       