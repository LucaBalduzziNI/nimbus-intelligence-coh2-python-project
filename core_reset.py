# Custom Modules
try:
    import modules.connector as connect
except Exception as e:
    from . import connector as connect

def reset_cache(table: str):
    """Resets one table of the app cache.

    Args:
        table (str): the table to be deleted
    """
    query = "DELETE FROM "
    connect.execute_query(query + table)