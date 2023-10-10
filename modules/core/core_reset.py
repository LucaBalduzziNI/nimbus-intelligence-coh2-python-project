# Custom Modules
try:
    from .. import connector as connect
except Exception as e:
    import modules.connector as connect

def reset_cache(table: str):
    """Resets one table of the app cache.

    Args:
        table (str): the table to be deleted
    """
    query = "DELETE FROM "
    connect.execute_query(query + table)