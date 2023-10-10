# Custom Modules
try:
    from modules import connector
    from modules.errors import *
    from modules.weather_api import get_weather
    from core_text_types import add_text
except Exception as e:
    raise e

def get_info(ip_address: str) -> str:
    
    # Getting weather info
    weather = get_weather(ip_address)
    hour = int(weather['local_time'].split(' ')[1].split(':')[0])
    temp = str(weather['temp_c']).split('.')[0]
    print(hour)
    # Selecting greeting
    if hour < 13:
        greeting = 'Good Morning'
    elif hour < 19:
        greeting = 'Good Afternoon'
    elif hour < 23:
        greeting = 'Good Evening'
    else:
        greeting = 'Good Night'
    
    info = greeting + ', the weather in ' + weather['city'] + ' is ' + weather['condition'] + ' with a temperature of ' + temp + ' degree celsius.'

    # Storing if not present
    try:
        add_text(info, 'en')
    except TextTypeIsAlreadyStored as e:
        pass

    return info

if __name__ == '__main__':
    print(get_info('95.231.206.38'))

