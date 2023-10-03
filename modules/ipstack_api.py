import requests
import json
import os


def resolve_ip(address)
    #IP Stack API Key
    API_KEY = os.getenv('IPSTACK_APIKEY')

    #Retrieve geolocation from IP stack
    data = requests.get(f"http://api.ipstack.com/{address}?access_key={API_KEY}")
    
    #Check if HTTP request succeeded
    if data.status_code == 200:      
        datajson = data.json()
        
        #Check if a language was resolved
        if datajson['location']['languages'] != null:
        
            #Return language code
            return datajson['location']['languages'][0]['name']
            
        else:
        raise Exception("No language was resolved")
    
    else:
    raise Exception("Connection error")
       