# Custom Modules
try:
    from modules import connector
    from modules.errors import *
    from modules.weather_api import get_weather
    from core_text_types import add_text
except Exception as e:
    raise e

def get_info(ip_address: str) -> str:
    weather = get_weather(ip_address)
    hour = weather['local_time'].split(' ')[1].split(':')[0]
    if hour < '12':
        greeting = 'Good Morning'
    elif hour < '20':
        greeting = 'Good Evening'
    else: 
        greeting = 'Good Night'
    
    info = greeting + ', the weather in ' + weather['city'] + ' is ' + weather['condition'] + ' with a temperature of ' + str(weather['temp_c']).split('.')[0] + ' degree celsius.'

    try:
        add_text(info, 'en')
    except TextTypeIsAlreadyStored as e:
        pass
    return info

