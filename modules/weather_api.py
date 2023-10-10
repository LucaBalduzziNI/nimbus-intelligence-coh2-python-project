# Modules
import requests

# Custom Modules
try:
    import secret_stuff
    from errors import *
except Exception as e:
    from . import secret_stuff
    from .errors import *

def get_weather(ip_address: str) -> dict:
    """Fetches informations about weather by the location of the Ip address

    Args:
        ip_address (str): the ip to geolocalize

    Raises:
        ConnectionError: raised if the request to the API is not successfull

    Returns:
        dict: dictionary containing city, local_time, temp_c and condition of the weather
    """
    
    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q": ip_address}

    headers = {
	    "X-RapidAPI-Key": secret_stuff.WEATHER_API,
	    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json()
        city = data['location']['name']
        local_time = data['location']['localtime']
        temp_c = data['current']['temp_c']
        condition = data['current']['condition']['text']
        return {'city': city, 'local_time': local_time, 'temp_c': temp_c, 'condition': condition}
    else:
        raise ConnectionError()

if __name__ == '__main__':
    print(get_weather('93.35.144.90'))
