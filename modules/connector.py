# Modules
from snowflake import connector
from typing import List

# Custom Modules
try:
    import secret_stuff
except Exception as e:
    from . import secret_stuff

def execute_query(query: str, params: tuple = None) -> List[dict]:
    """This method interacts with snowflake through the snowflake connector, handling the opening and closing of the connection.

    Raises:
        Exception: any exception that could arise in the execution

    Returns:
        List[dict]: The result of the query. It can be data (if a select statement is given) or informations about the given command. 
    """
    # Creating the connector and using it
    with connector.connect(
            user = secret_stuff.SNOWSQL_USR,
            password = secret_stuff.SNOWSQL_PSW,
            account = secret_stuff.SNOWSQL_ACC,
            warehouse = secret_stuff.SNOWSQL_WH,
            database = secret_stuff.SNOWSQL_DB,
            schema = secret_stuff.SNOWSQL_SCH
        ) as conn:
        # Catching any exception to return to the caller
        try:
            cur = conn.cursor(connector.DictCursor)
            return cur.execute(query, params).fetchall()
        except Exception as e:
            raise e