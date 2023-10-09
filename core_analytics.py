import pandas as pd

#Custom Modules
try:
    import modules.connector as connect
except Exception as e:
    from . import connector as connect


def ip_analytics():
    query = f"SELECT IP_ADDRESS, COUNTRY_CODE FROM IP_ADDRESSES"
    results = connect.execute_query(query)
    addresses = pd.DataFrame(data=results, columns=["IP_ADDRESS", "COUNTRY_CODE"])
    return addresses
