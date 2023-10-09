# Modules
from typing import List

# Custom Modules
try:
    from modules import connector
    from modules.errors import *
except Exception as e:
    raise e

def get_texts() -> List[dict]:
    query = "SELECT source_text, source_lang_code FROM text_types"
    return connector.execute_query(query)

def add_text(text: str, source_lang: str):
    query = f"SELECT source_text FROM text_types WHERE source_text = '{text}'"

    result = connector.execute_query(query)
    if not text or not source_lang:
        raise Exception('Values must not be None!')
    elif text == '' or source_lang == '':
        raise Exception('Values must contain chars!')
    elif len(result) == 0:
        query = f"INSERT INTO text_types (source_text, source_lang_code) VALUES ('{text}', '{source_lang}')"
        connector.execute_query(query)
    else:
        raise TextTypeIsAlreadyStored(text)

if __name__ == '__main__':
    print(connector.execute_query("UPDATE text_types SET source_lang_code = 'en' WHERE source_lang_code = 'Good Night'"))