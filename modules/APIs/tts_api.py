# Modules
import requests

# Custom Modules
try:
    from .. import secret_stuff
    from ..errors import *
except Exception as e:
    import modules.secret_stuff
    from modules.errors import *

def check_if_spoken(language_code: str):

    """Checks if the language is available to speak
    Args:
        language_code (str): Language code to be checked for speaking capabilities

    Returns:
        bool: Whether the language can be spoken by the API

    Raises:
        ConnectionError: raised if connection with the API was not successful
      
    """
    url = "https://text-to-speech27.p.rapidapi.com/speech"

    headers = {
        "X-RapidAPI-Key": secret_stuff.TTS_API_KEY,
        "X-RapidAPI-Host": "text-to-speech27.p.rapidapi.com"
    }

    # Checking if the language can be spoken
    response = requests.get(url + '/lang', headers=headers)

    # Checking if the language can be spoken
    if response.status_code == 200:
        if language_code not in response.json().keys():
            return(False)
        else:
            return(True)
    else:
        raise ConnectionError()


def text_to_speech(text: str, lang: str) -> bytes:
    """This function fetches an API to perform TTS with the given text.

    Args:
        text (str): The text to perform TTS on
        lang (str): The language of the TTS converision

    Raises:
        TextIsBlank: raised if the given text is an empty string
        LanguageCantBeSpoken: raised if the given language cannot be TTS by the API
        ConnectionError: raised if the connection with the API was not successful

    Returns:
        bytes: The audio file in bytes
    """

    url = "https://text-to-speech27.p.rapidapi.com/speech"

    headers = {
        "X-RapidAPI-Key": secret_stuff.TTS_API_KEY,
        "X-RapidAPI-Host": "text-to-speech27.p.rapidapi.com"
    }

    # Text is a blank string
    if len(text) == 0:
        raise TextIsBlank()

    #Commented as this should be handled outside the API through the cache
    #if(check_if_spoken) == False:
        #raise LanguageCantBeSpoken(lang)

    # Text to be translated
    params = {"text": text, "lang": lang}

    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.content
    else:
        raise ConnectionError()

# Testing Purposes
if __name__ == '__main__':

    with open('myfile.wav', mode='bw') as f:
        f.write(text_to_speech('ciao', 'en-us'))
    f.close()