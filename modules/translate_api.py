# Modules
import requests
import json
import os

# Custom Modules
try:
    import secret_stuff
    from errors import *
except Exception as e:
    from . import secret_stuff
    from .errors import *

def translate_string(original_string, language_code, source_language = "en"):
   # Check if string even needs translating
    if language_code != source_language:

        # Check if language is available within the API
        url = "https://google-translate1.p.rapidapi.com/language/translate/v2/languages"

        headers = {
            "Accept-Encoding": "application/gzip",
            "X-RapidAPI-Key": secret_stuff.GOOGLE_TRANS_API_KEY,
            "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)


        languages = response.json()
        
        languages['data']['languages']
        language_list = []

        for language in languages['data']['languages']:
            language_list.append(language['language'])
        
        if language_code in language_list and source_language in language_list:
            
            #Translate the string
            url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

            payload = {
                "q": original_string,
                "target": language_code,
                "source": source_language
            }
            headers = {
                "content-type": "application/x-www-form-urlencoded",
                "Accept-Encoding": "application/gzip",
                "X-RapidAPI-Key": "716e9bf1b0mshad02c68002e32bdp142e29jsn934d45a3cf44",
                "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
            }

            response = requests.post(url, data=payload, headers=headers)
            translation = response.json()

            if 'data' in translation and translation['data']['translations'] is not None: 
                return(translation['data']['translations'][0]['translatedText'])
            
            else:
                raise Exception("Translation API failure")
            
            
        else:
            raise Exception("The language can not be translated")
    else:
       return(original_string)

print(translate_string("This is a test", "en", "en"))
#print(translate_string("This is a test", "it"))
#print(translate_string("This is a test", "nl"))
#print(translate_string("This is a test", "ja"))