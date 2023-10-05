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


