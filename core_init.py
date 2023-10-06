# Modules
import modules.ipstack_api as ipstack
import modules.translate_api as translate
import modules.tts_api as tts
import modules.ipify_api as ipify
import modules.connector as connect

# Custom Modules
try:
    import modules.secret_stuff
except Exception as e:
    from . import secret_stuff

def init_app(userIP: str = None):
    """This method initialized the application for the user.

    Args:
        Userip (str): IP address. Will be retrieved if not presented.

    Raises:
        e: _description_

    Returns:
            list: Location details
                [   str: Country name
                    str: Country flag
                ]

            list: Details of languages spoken in country
                [   str: Language code
                    bool: Language can be translated
                    bool: Language can be spoken
                ]
            
            str: Preferred language
    """

    #Retrieve userIP if none was given
    if userIP == None:
        userIP = str(ipify.get_ip())
    userLocation = []

    #Check if IP Address is cached
    query = f"SELECT ip_address, country_code, pref_lang_code FROM IP_ADDRESSES WHERE IP_ADDRESS = '{userIP}'"
    results = connect.execute_query(query)
    if len(results) == 1:
        #Retrieve cached values for IP
        userCountry = results[0]['COUNTRY_CODE']
        userLanguage = results[0]['PREF_LANG_CODE']
    else:
        #Retrieve new values for IP and cache them
        userLocation = ipstack.resolve_ip(userIP)
        userCountry = userLocation['country_code']
        userLanguage = userLocation['languages'][0] 
        query = f"INSERT INTO IP_ADDRESSES (ip_address, country_code, pref_lang_code) VALUES('{userIP}','{userCountry}','{userLanguage}')"
        connect.execute_query(query)
    
    #Check if country is known in the database
    query = f"SELECT country_code, country_name, country_flag FROM COUNTRIES WHERE COUNTRY_CODE = '{userCountry}'"
    results = connect.execute_query(query)
    if len(results) == 1:
        #Retrieve cached values for country
        countryName = results[0]['COUNTRY_NAME']
        countryFlag = results[0]['COUNTRY_FLAG']
    else:
        #Retrieve new values for country and cache them       
        if len(userLocation) == 0:
            #In case the IP was known but the country is not (this should not normally happen)
            userLocation = ipstack.resolve_ip(userIP)
        countryName = userLocation['country_name']
        countryFlag = userLocation['country_flag']
        query = f"INSERT INTO COUNTRIES (country_code, country_name, country_flag) VALUES('{userCountry}', '{countryName}', '{countryFlag}')"
        connect.execute_query(query)

    #Check if languages spoken in country are known
    query = f"SELECT country_code, language_code FROM LANGUAGES_COUNTRY WHERE COUNTRY_CODE = '{userCountry}'"
    results = connect.execute_query(query)
    if len(results) >= 1:
        #Retrieve cached languages
        language_list = []
        for result in results:
            language_list.append(result['LANGUAGE_CODE'])
    else:
        #Retrieve new list of languages and cache them
        if len(userLocation) == 0:
            #In case the IP was known but the country is not (this should not normally happen)
            userLocation = ipstack.resolve_ip(userIP)
        language_list = userLocation['languages']
        for language in language_list:
            query = f"INSERT INTO LANGUAGES_COUNTRY (country_code, language_code) VALUES ('{userCountry}', '{language}')"
            connect.execute_query(query)

    #Check if each language is known to be translatable and spoken
    language_list_details = []
    for language in language_list:
        query = f"SELECT language_code, can_be_translated, can_be_spoken FROM LANGUAGES WHERE LANGUAGE_CODE = '{language}'"
        results = connect.execute_query(query)
    if len(results) == 1:
        #Retrieve cached knowledge on languages
        language_list_details.append([language, result['CAN_BE_TRANSLATED'], result['CAN_BE_SPOKEN']])
    else:
        #Retrieve new list of knowledge on languages and cache them
        can_be_translated = tts.check_if_spoken(language)
        can_be_spoken = translate.check_if_translatable(language)
        language_list_details.append([language, can_be_translated, can_be_spoken])
        query = f"INSERT INTO LANGUAGES (language_code, can_be_translated, can_be_spoken) VALUES ('{language}', '{can_be_translated}', '{can_be_spoken}')"
        connect.execute_query(query)

    return [countryName, countryFlag], language_list_details, userLanguage


init_app()
