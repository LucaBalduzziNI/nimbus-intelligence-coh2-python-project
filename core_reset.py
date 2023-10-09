# Custom Modules
try:
    import modules.connector as connect
except Exception as e:
    from . import connector as connect

def reset_cache():
    query = "DELETE FROM "
    tables = ['Countries', 'IP_Addresses', 'Languages_Country', 'Languages', 'Text_types', 'Translations']
    for table in tables:
        connect.execute_query(query + table)