import pandas as pd

#Custom Modules
try:
    import modules.connector as connect
except Exception as e:
    from . import connector as connect


def ip_analytics():
    query = f"SELECT COUNT(IP_ADDRESS) FROM IP_ADDRESSES"
    results = connect.execute_query(query)
    return results[0]['COUNT(IP_ADDRESS)']

def country_code_analytics():
    query = f"SELECT COUNTRY_CODE, COUNT(IP_ADDRESS) AS IPCOUNT FROM IP_ADDRESSES GROUP BY COUNTRY_CODE"
    results = connect.execute_query(query)
    addresses = pd.DataFrame(data=results, columns=["COUNTRY_CODE", "IPCOUNT"])
    return addresses

def country_list_analytics():
    query = f"SELECT DISTINCT COUNTRY_CODE FROM IP_ADDRESSES"
    results = connect.execute_query(query)
    countries = pd.DataFrame(data=results)
    return countries

def country_language_analytics(country_code):
    query = f"SELECT PREF_LANG_CODE, COUNT(COUNTRY_CODE) AS COUNTRYCOUNT FROM IP_ADDRESSES WHERE COUNTRY_CODE = '{country_code}' GROUP BY PREF_LANG_CODE"
    results = connect.execute_query(query)
    languages = pd.DataFrame(data=results, columns=["PREF_LANG_CODE", "COUNTRYCOUNT"])
    return languages