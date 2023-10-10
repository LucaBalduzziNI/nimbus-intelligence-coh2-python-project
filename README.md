# Nimbus Intelligence Cohort2 Python-Snowflake Project: SkySpeak

This repository is a Python-Snowflake project developed during the Nimbus Intelligence Academy.

## Initialization

Required for running this app is a password file named modules/secret_stuff.py containing the following:

```
IP_STACK_API_KEY = Your personal API key for IPStack (https://ipstack.com/)
TTS_API_KEY = Your personal API key for Kelvin's Text to Speech API (https://rapidapi.com/kelvin2go/api/text-to-speech27)
GOOGLE_TRANS_API_KEY = Your personal API key for Google Translate (https://rapidapi.com/googlecloud/api/google-translate1)
WEATHER_API = Your personal API key for Weather API (https://rapidapi.com/weatherapi/api/weatherapi-com)

SNOWSQL_USR = Your Snowflake username
SNOWSQL_PSW = Your Snowflake password
SNOWSQL_ACC = Your Snowflake server location
SNOWSQL_WH = Your Snowflake warehouse
SNOWSQL_DB = Your Snowflake database
SNOWSQL_SCH = Your Snowflake schema
```

## Requirements Installation

Requirements for python can be obtained using the command:

```
pip install -r ./requirements.txt
```

## Launching the App

The app can be launched by typing:

```
python run ./Home.py
```