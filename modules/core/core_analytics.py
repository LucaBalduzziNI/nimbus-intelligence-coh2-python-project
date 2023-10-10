import pandas as pd

#Custom Modules
try:
    from .. import connector as connect
except Exception as e:
    import modules.connector as connect


def ip_analytics():
    #IPs per country
    query = f"SELECT COUNT(IP_ADDRESS) FROM IP_ADDRESSES"
    results = connect.execute_query(query)
    return results[0]['COUNT(IP_ADDRESS)']

def country_code_analytics():
    #Total resolved IP addresses cached
    query = f"SELECT COUNTRY_NAME, COUNT(IP_ADDRESS) AS IPCOUNT FROM IP_ADDRESSES INNER JOIN COUNTRIES ON IP_ADDRESSES.COUNTRY_CODE = COUNTRIES.COUNTRY_CODE GROUP BY COUNTRY_NAME"
    results = connect.execute_query(query)
    addresses = pd.DataFrame(data=results, columns=["COUNTRY_NAME", "IPCOUNT"])
    return addresses

def country_list_analytics():
    #List of countries
    query = f"SELECT DISTINCT IP_ADDRESSES.COUNTRY_CODE AS COUNTRY_CODE, COUNTRY_NAME FROM IP_ADDRESSES INNER JOIN COUNTRIES ON IP_ADDRESSES.COUNTRY_CODE = COUNTRIES.COUNTRY_CODE"
    results = connect.execute_query(query)
    #countries = pd.DataFrame(data=results)
    return results

def country_language_analytics(country_code):
    #Preferred languages per country
    query = f"SELECT PREF_LANG_CODE, COUNT(COUNTRY_CODE) AS COUNTRYCOUNT FROM IP_ADDRESSES WHERE COUNTRY_CODE = '{country_code}' GROUP BY PREF_LANG_CODE"
    results = connect.execute_query(query)
    languages = pd.DataFrame(data=results, columns=["PREF_LANG_CODE", "COUNTRYCOUNT"])
    return languages

def chunk_analytics():
    #Total cached sentence chunks for translation
    query = f"SELECT COUNT(TEXT_ID) FROM TEXT_TYPES"
    results = connect.execute_query(query)
    return results[0]['COUNT(TEXT_ID)']

def translate_analytics():
    #Total cached translations
    query = f"SELECT COUNT(*) FROM TRANSLATIONS"
    results = connect.execute_query(query)
    return results[0]['COUNT(*)']

def translate_chunk():
    #Number of different translations per chunk
    query = f"SELECT TEXT_ID, COUNT(LANGUAGE_CODE) AS LANGUAGECOUNT FROM TRANSLATIONS GROUP BY TEXT_ID"
    results = connect.execute_query(query)
    chunks = pd.DataFrame(data=results, columns=["TEXT_ID", "LANGUAGECOUNT"])
    return chunks

def chunk_language():
    #Number of translated chunks per language
    query = f"SELECT COUNT(TEXT_ID) AS TEXTCOUNT, LANGUAGE_CODE FROM TRANSLATIONS GROUP BY LANGUAGE_CODE"
    results = connect.execute_query(query)
    chunks = pd.DataFrame(data=results, columns=["TEXTCOUNT", "LANGUAGE_CODE"])
    return chunks

def requests_analytics():
    #Total requests logged
    query = f"SELECT COUNT(*) FROM REQUEST_LOG"
    results = connect.execute_query(query)
    return results[0]['COUNT(*)']

def cache_analytics():
    #Total cached requests logged
    query = f"SELECT COUNT(*) FROM REQUEST_LOG WHERE CACHED = TRUE"
    results = connect.execute_query(query)
    return results[0]['COUNT(*)']

def cache_details():
    #Graphable cache details
    query = f"SELECT API_CODE, CACHED, TIMESTAMP FROM REQUEST_LOG"
    results = connect.execute_query(query)
    cache = pd.DataFrame(data=results, columns=["API_CODE", "CACHED", "TIMESTAMP"])
    return cache