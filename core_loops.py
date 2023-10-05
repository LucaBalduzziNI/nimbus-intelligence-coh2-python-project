import modules.ipstack_api as ipstack
import modules.translate_api as translate
import modules.tts_api as tts
import modules.ipify_api as ipify


userIP = ipify.get_ip()

#Check if IP Address is cached
query = f"SELECT ip_address, country_code, pref_lang_code FROM IP_ADDRESSES WHERE IP_ADDRESS = {userIP}"

#if len(results) = 1
userCountry = results[0]['userCountry']
userLanguage = results[0]['pref_lang_code']

#If not, resolve IP and insert
userLocation = ipstack.resolve_ip(userIP)
userCountry = userLocation['country_code']
userLanguage = userLocation['languages'][0]
query = f"INSERT INTO IP_ADDRESSES (ip_address, country_code, pref_lang_code) VALUES({userIP},{userLocation},{userLanguage})"

#Check if country is known in the database
query = f"SELECT country_code, country_name, country_flag FROM COUNTRIES WHERE COUNTRY_CODE = {userCountry}"

#if len(results) = 1
countryName = results[0]['country_name']
countryFlag = results[0]['country_flag']

#If not, store results from resolving
countryName = userLocation['country_name']
countryFlag = userLocation['country_flag']
query = f"INSERT INTO COUNTRIES (country_code, country_name, country_flag) VALUES({userCountry}, {countryName}, {countryFlag})"

#Check if languages spoken in country are known
query = f"SELECT country_code, language_code FROM LANGUAGES_COUNTRIES WHERE COUNTRY_CODE = {userCountry}"

#if len(results) >= 1
language_list = []

for result in results:
    language_list.append(result['language_code'])

#If not, store results from resolving
language_list = userLocation['languages']
for language in language_list:
    query = f"INSERT INTO LANGUAGES_COUNTRY (country_code, language_code) VALUES ({userCountry}, {language})"


#Check if each language is known to be translatable and spoken
language_list_details = []
for language in language_list:
    query = f"SELECT language_code, can_be_translated, can_be_spoken FROM LANGUAGES WHERE LANGUAGE_CODE = {language}"
    #if len(results) = 1
    language_list_details.append([language, result['can_be_translated'], result['can_be_spoken']])
    #else (language is not known in the database)
    can_be_translated = tts.check_if_spoken(language)
    can_be_spoken = translate.check_if_translatable(language)
    language_list_details.append(language, can_be_translated, can_be_spoken)
    query = f"INSERT INTO LANGUAGES (language_code, can_be_translated, can_be_spoken) VALUES ({language})"

    #If text is neither translatable nor speakable everything below this is moot

#sample source text
source_text = "Hello, this is a test"
source_lang_code = "en"

#Check if the source text is known
query = f"SELECT text_id FROM TEXT_TYPES WHERE SOURCE_TEXT = {source_text} AND SOURCE_LANG_CODE = {source_lang_code}"
#if len(results) == 1
text_id = results['text_id']
#if len(results) == 0 and can_be_translated == 1
query = f"INSERT INTO TEXT_TYPES (source_text, source_lang_code) VALUES ({source_text}, {source_lang_code})"
query = f"SELECT text_id FROM TEXT_TYPES WHERE SOURCE_TEXT = {source_text} AND SOURCE_LANG_CODE = {source_lang_code}"


query = f"SELECT target_text, target_audio_bin FROM TRANSLATIONS WHERE TEXT_ID = {text_id} AND language_code = {language}"








