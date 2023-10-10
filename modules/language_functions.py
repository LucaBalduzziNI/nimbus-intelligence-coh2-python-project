# Custom Modules
try:
    import secret_stuff
    import connector as connect
    import translate_api as translate
    import tts_api as tts
    from errors import *
except Exception as e:
    from . import secret_stuff
    from . import connector as connect
    from . import translate_api as translate
    from . import tts_api as tts
    from .errors import *

def translate_string(original_string: str, language_code: str, source_language: str = "en") -> str:
    """Translates a string through the API or retrieve translation from cache

    Args:
        original_string (str): Text to be translated
        language_code (str): Language code for the string to be translated to.
        source_language (str, optional): Source language the text derives from. Defaults to "en".

    Raises:
        APITranslationError: _description_
        LanguageCantBeTranslated: _description_

    Returns:
        str: The translated text
    """

    # Check if language can be translated - These values were collected during initialization of the app
    query = f"SELECT can_be_translated FROM languages WHERE language_code = '{language_code}'"
    results = connect.execute_query(query)
    if results[0]['CAN_BE_TRANSLATED'] == True:
        #Check if the string is available for translation within the app
        query = f"SELECT text_id from text_types WHERE source_text = '{original_string}' AND source_lang_code = '{source_language}'"
        results = connect.execute_query(query)
        if len(results) == 1:
            text_id = results[0]['TEXT_ID']
            #Check if the translation of the string is already known
            query = f"SELECT target_txt FROM translations WHERE text_id = '{text_id}' and language_code = '{language_code}'"
            results = connect.execute_query(query)
            if len(results) == 1:
                #Retrieve translation from cache
                translation = results[0]['TARGET_TXT']
                
                #Log cached request
                query = f"INSERT INTO REQUEST_LOG (API_CODE, CACHED, TIMESTAMP) VALUES ('TRANSLATE', TRUE, current_timestamp())"
                connect.execute_query(query)
            else:
                #Translate and cache
                translation = translate.translate_string(original_string, language_code, source_language)
                query = f"INSERT INTO translations (language_code, text_id, target_txt) VALUES ('{language_code}', '{text_id}', '{translation}')"
                connect.execute_query(query)

                #Log non-cached request
                query = f"INSERT INTO REQUEST_LOG (API_CODE, CACHED, TIMESTAMP) VALUES ('TRANSLATE', FALSE, current_timestamp())"
                connect.execute_query(query)
        else:
            raise Exception("String is not in present in text types")
    else:
        raise LanguageCantBeTranslated(language_code)
    return translation

def text_to_speech(text: str, lang: str) -> bytes:
    """Speaks a text through an API or retrieves the audio from cache

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
    # Check if language can be spoken - These values were collected during initialization of the app
    query = f"SELECT can_be_spoken FROM languages WHERE language_code = '{lang}'"
    results = connect.execute_query(query)
    if results[0]['CAN_BE_SPOKEN'] == True:
        #Check if the translation of the string is already known
        query = f"SELECT target_audio_bin FROM translations WHERE target_txt = '{text}' and language_code = '{lang}'"
        results = connect.execute_query(query)
        if len(results) == 1:
            #Check if the string was also spoken already
            if results[0]['TARGET_AUDIO_BIN'] != None:
                speech = results[0]['TARGET_AUDIO_BIN']

                #Log cached request
                query = f"INSERT INTO REQUEST_LOG (API_CODE, CACHED, TIMESTAMP) VALUES ('TTS', TRUE, current_timestamp())"
                connect.execute_query(query)

            else:
                #Speak and cache
                speech = tts.text_to_speech(text, lang)                    
                connect.execute_query('update translations set target_audio_bin = %s where target_txt = %s and language_code = %s', (speech, text, lang))

                #Log non-cached request
                query = f"INSERT INTO REQUEST_LOG (API_CODE, CACHED, TIMESTAMP) VALUES ('TTS', FALSE, current_timestamp())"
                connect.execute_query(query)
        
        else:
            raise Exception("String has not yet been translated before being spoken")           

    else:
        raise LanguageCantBeSpoken(lang)
    return speech

if __name__ == '__main__':

    with open('myfilegerman.wav', mode='bw') as f:
        f.write(text_to_speech(translate_string("Good Morning", "de"),"de"))
    f.close()