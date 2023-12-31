# Modules
from collections import namedtuple

# Custom Modules
try:
    from .. import secret_stuff
    from ..APIs import ipstack_api as ipstack
    from ..APIs import translate_api as translate   
    from ..APIs import tts_api as tts
    from ..APIs import ipify_api as ipify
    from .. import connector as connect
except Exception as e:
    import modules.secret_stuff
    import modules.APIs.ipstack_api as ipstack
    import modules.APIs.translate_api as translate 
    import modules.APIs.tts_api as tts
    import modules.APIs.ipify_api as ipify
    import modules.connector as connect

# Custom Tuples 
ip_country = namedtuple('ip_country', [
    'ip_address',
    'pref_lang_code',
    'country_code',
    'country_name',
    'country_flag',
    'lang_details'
])

def init_app(userIP: str = None) -> ip_country:
    """This function initialized information for the user.

    Args:
        userIP (str, optional): Ip address which will be retrieved if not given. Defaults to None.

    Returns:
        ip_country: Tuple containing information about user_ip and country.
    """

    # Retrieve userIP if none was given
    if userIP == None:
        userIP = str(ipify.get_ip())
    userLocation = []

    # Check if IP Address is cached
    query = f"SELECT ip_address, country_code, pref_lang_code FROM IP_ADDRESSES WHERE IP_ADDRESS = '{userIP}'"
    results = connect.execute_query(query)
    if len(results) == 1:
        # Retrieve cached values for IP
        userCountryCode = results[0]['COUNTRY_CODE']
        userLanguage = results[0]['PREF_LANG_CODE']
    else:
        # Retrieve new values for IP and cache them
        userLocation = ipstack.resolve_ip(userIP)
        userCountryCode = userLocation['country_code']
        userLanguage = userLocation['languages'][0][0] if len(userLocation['languages']) == 1 else None
        query = f"INSERT INTO IP_ADDRESSES (ip_address, country_code, pref_lang_code) VALUES('{userIP}','{userCountryCode}','{userLanguage}')"
        connect.execute_query(query)
    
    # Check if country is known in the database
    query = f"SELECT country_code, country_name, country_flag FROM COUNTRIES WHERE COUNTRY_CODE = '{userCountryCode}'"
    results = connect.execute_query(query)
    if len(results) == 1:
        # Retrieve cached values for country
        countryName = results[0]['COUNTRY_NAME']
        countryFlag = results[0]['COUNTRY_FLAG']
    else:
        #Retrieve new values for country and cache them       
        if len(userLocation) == 0:
            #In case the IP was known but the country is not (this should not normally happen)
            userLocation = ipstack.resolve_ip(userIP)
        countryName = userLocation['country_name']
        countryFlag = userLocation['country_flag']
        query = f"INSERT INTO COUNTRIES (country_code, country_name, country_flag) VALUES('{userCountryCode}', '{countryName}', '{countryFlag}')"
        connect.execute_query(query)

    # Check if languages spoken in country are known
    query = f"SELECT country_code, languages_country.language_code, native_name FROM LANGUAGES_COUNTRY LEFT JOIN LANGUAGES ON languages_country.language_code = languages.language_code WHERE COUNTRY_CODE = '{userCountryCode}' "
    results = connect.execute_query(query)
    if len(results) >= 1:
        # Retrieve cached languages
        language_list = []
        for result in results:
            language_list.append([result['LANGUAGE_CODE'], result['NATIVE_NAME']])
    else:
        # Retrieve new list of languages and cache them
        if len(userLocation) == 0:
            # In case the IP was known but the country is not (this should not normally happen)
            userLocation = ipstack.resolve_ip(userIP)
        language_list = userLocation['languages']
        for language in language_list:
            languageCode = language[0]
            query = f"INSERT INTO LANGUAGES_COUNTRY (country_code, language_code) VALUES ('{userCountryCode}', '{languageCode}')"
            connect.execute_query(query)

    # Check if each language is known to be translatable and spoken
    language_list_details = []
    for language in language_list:
        languageCode = language[0]
        query = f"SELECT language_code, native_name, can_be_translated, can_be_spoken FROM LANGUAGES WHERE LANGUAGE_CODE = '{languageCode}'"
        results = connect.execute_query(query)
        if len(results) == 1 and results[0]['NATIVE_NAME'] != None:
            # Retrieve cached knowledge on languages
            can_be_translated = results[0]['CAN_BE_TRANSLATED']
            can_be_spoken = results[0]['CAN_BE_SPOKEN']
            nativeName = results[0]['NATIVE_NAME']
            language_list_details.append((languageCode, nativeName, can_be_translated, can_be_spoken))
        else:
            # Retrieve new list of knowledge on languages and cache them
            if len(userLocation) == 0:
            # In case the languages were known but the native name was not (this should not normally happen)
                userLocation = ipstack.resolve_ip(userIP)

            can_be_translated = translate.check_if_translatable(languageCode)
            can_be_spoken = tts.check_if_spoken(languageCode)
            nativeName = language[1]
            language_list_details.append((languageCode, nativeName, can_be_translated, can_be_spoken))
            query = f"INSERT INTO LANGUAGES (language_code, native_name, can_be_translated, can_be_spoken) VALUES ('{languageCode}', '{nativeName}', '{can_be_translated}', '{can_be_spoken}')"
            connect.execute_query(query)

    return ip_country(userIP, userLanguage, userCountryCode, countryName, countryFlag, language_list_details)

if __name__ == '__main__':
    print(init_app())
