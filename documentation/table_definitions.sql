CREATE TABLE Countries(
    country_code varchar,
    country_name varchar,
    country_flag varchar,
    language_code varchar
);

CREATE TABLE IP_Addresses(
    ip_address varchar,
    country_code varchar
);

CREATE TABLE Languages(
    language_code varchar,
    can_be_translated boolean,
    can_be_spoken boolean
);

CREATE TABLE Text_types(
    text_id int NOT NULL AUTOINCREMENT,
    source_text varchar,
    language_code varchar
);

CREATE TABLE Translations(
    language_code varchar,
    text_id int,
    target_txt varchar,
    target_audio varchar
);