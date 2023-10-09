# Custom Modules
try:
    import modules.connector as connect
except Exception as e:
    from . import connector as connect

def reset_cache(table: str):
    query = "DELETE FROM "
    connect.execute_query(query + table)