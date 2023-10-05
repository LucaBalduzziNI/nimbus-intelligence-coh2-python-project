CREATE OR REPLACE TABLE Countries(
    country_code varchar,
    country_name varchar,
    country_flag varchar
);

CREATE OR REPLACE TABLE IP_Addresses(
    ip_address varchar,
    country_code varchar,
    pref_lang_code varchar
);

CREATE OR REPLACE TABLE Languages_Country(
    language_code varchar,
    country_code varchar
);

CREATE OR REPLACE TABLE Languages(
    language_code varchar,
    can_be_translated boolean,
    can_be_spoken boolean
);

CREATE OR REPLACE TABLE Text_types(
    text_id int NOT NULL AUTOINCREMENT,
    source_text varchar,
    source_lang_code varchar
);

CREATE OR REPLACE TABLE Translations(
    language_code varchar,
    text_id int,
    target_txt varchar,
    target_audio_bin binary
);

