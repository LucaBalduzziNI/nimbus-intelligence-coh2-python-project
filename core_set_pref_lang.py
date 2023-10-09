# Custom Modules
try:
    import modules.connector as connect
except Exception as e:
    from . import connector as connect

def set_pref_lang(ip_address: str, lang_code: str):
    query = f"UPDATE IP_ADDRESSES SET pref_lang_code = '{lang_code}' WHERE ip_address = '{ip_address}'"
    connect.execute_query(query)