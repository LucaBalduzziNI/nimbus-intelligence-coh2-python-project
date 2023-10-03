# Modules
import requests
import json
import os

# Custom Modules
try:
    from . import secret_stuff
except Exception as e:
    import secret_stuff

def translate_string(original_string, language_code):
    
    # Check if language is available within the API
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2/languages"

    headers = {
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": secret_stuff.GOOGLE_TRANS_API_KEY,
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    print(response.content)
    #print(response.json())

translate_string("This is a test", "nl")