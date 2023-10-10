# Modules
from typing import List
from collections import namedtuple

# Custom Modules
try:
    from modules import connector
    from modules.errors import *
except Exception as e:
    raise e

def get_texts() -> List[dict]:
    """Retrieves all text types form the DB.

    Returns:
        List[dict]: the list of text_types
    """
    query = "SELECT source_text, source_lang_code FROM text_types"
    return connector.execute_query(query)

def add_text(text: str, source_lang: str):
    """Adds a text_type to the DB.

    Args:
        text (str): the text_type to be stored.
        source_lang (str): the source language of the text

    Raises:
        TypeError: raised if one or both values are None
        ValueError: raised if one or both values are empty strings
        TextTypeIsAlreadyStored: raised if the text is already stored in the DB
    """

    # Checking values
    if not text or not source_lang:
        raise TypeError('Values must not be None!')
    elif text == '' or source_lang == '':
        raise ValueError('Values must contain chars!')
    
    query = f"SELECT source_text FROM text_types WHERE source_text = '{text}'"

    result = connector.execute_query(query)

    # insert the text if not already present
    if len(result) == 0:
        query = f"INSERT INTO text_types (source_text, source_lang_code) VALUES ('{text}', '{source_lang}')"
        connector.execute_query(query)
    else:
        raise TextTypeIsAlreadyStored(text)

if __name__ == '__main__':
    print(connector.execute_query("UPDATE text_types SET source_lang_code = 'en' WHERE source_lang_code = 'Good Night'"))