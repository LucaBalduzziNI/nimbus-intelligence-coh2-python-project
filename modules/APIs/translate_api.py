# Modules
import requests

# Custom Modules
try:
    from .. import secret_stuff
    from ..errors import *
except Exception as e:
    import modules.secret_stuff
    from modules.errors import *

def check_if_translatable(language_code: str):
    """Checks if the language is available to translate
    Args:
        language_code (str): Language code to be checked for translation capabilities

    Returns:
        bool: Whether the language can be translated by the API
      
    """
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
        
    if language_code in language_list:
        return(True)
    else:
        return(False)


def translate_string(original_string: str, language_code: str, source_language: str = "en") -> str:
    """Translates a string from a language to another.

    Args:
        original_string (str): Text to be translated
        language_code (str): Language code for the string to be translated to.
        source_language (str, optional): Source language the text derives from. Defaults to "en".

    Raises:
        APITranslationError: error when translating the text

    Returns:
        str: The translated text
    """

    # Check if string even needs translating
    if language_code != source_language:

        # Check if language is available within the API
        #This check is commented out as this is handled properly through the cache now
        #if (check_if_translatable(language_code) and check_if_translatable(source_language)):
            
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
                "X-RapidAPI-Key": secret_stuff.GOOGLE_TRANS_API_KEY,
                "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
            }

            response = requests.post(url, data=payload, headers=headers)
            translation = response.json()

            if 'data' in translation and translation['data']['translations'] is not None: 
                return(translation['data']['translations'][0]['translatedText'])
            
            else:
                raise APITranslationError(source_language, language_code)
        #else:
            #raise LanguageCantBeTranslated(language_code)
    else:
       return original_string

if __name__ == "__main__":
    print(translate_string("This is a test", "nl", "en"))
    #print(translate_string("This is a test", "it"))
    #print(translate_string("This is a test", "nl"))
    #print(translate_string("This is a test", "ja"))