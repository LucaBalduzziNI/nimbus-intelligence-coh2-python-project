# Custom Modules
try:
    from .. import connector as connect
except Exception as e:
    import modules.connector as connect

def set_pref_lang(ip_address: str, lang_code: str):
    """Sets the preffered language associated to the ip.

    Args:
        ip_address (str): ip address to make the change on
        lang_code (str): language code to be set as preferred
    """
    query = f"UPDATE IP_ADDRESSES SET pref_lang_code = '{lang_code}' WHERE ip_address = '{ip_address}'"
    connect.execute_query(query)