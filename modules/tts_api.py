# Modules
import requests

# Custom Modules
try:
    import secret_stuff
    from errors import *
except Exception as e:
    from . import secret_stuff
    from .errors import *

def text_to_speech(text: str, lang: str) -> bytes:
    """This function fetches an API to perform TTS with the given text.

    Args:
        text (str): The text to perform TTS on
        lang (str): The language of the TTS converision

    Raises:
        TextIsBlank: _description_
        LanguageCantBeSpoken: _description_
        ConnectionError: _description_
        ConnectionError: _description_

    Returns:
        bytes: The audio file in bytes
    """

    url = "https://text-to-speech27.p.rapidapi.com/speech"

    headers = {
        "X-RapidAPI-Key": secret_stuff.TTS_API_KEY,
        "X-RapidAPI-Host": "text-to-speech27.p.rapidapi.com"
    }

    # Text is a blank string
    if not text.isalnum():
        raise TextIsBlank()

    # Checking if the language can be spoken
    response = requests.get(url + '/lang', headers=headers)

    # Checking if the language can be spoken
    if response.status_code == 200:
        if lang not in response.json().keys():
            raise LanguageCantBeSpoken(lang)
    else:
        raise ConnectionError()

    # Text to be translated
    params = {"text": text, "lang": lang}

    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.content
    else:
        raise ConnectionError()

# Testing Purposes
if __name__ == '__main__':
    i = 0
    while i < 20:
        i += 1
        with open('myfile.wav', mode='bw') as f:
            f.write(text_to_speech('ciao', 'en-us'))
        f.close()