CREATE TABLE seasons (
    season_id int,
    season_no int,
    air_date_start text,
    air_date_end text

) CREATE TABLE episodes (
    episode_id int,
    season_id int,
    episode_no int,
    chronological_no int,
    title text,
    air_date text


DROP TABLE IF EXISTS quote;


CREATE TABLE IF NOT EXISTS quotes (
    quote_id INTEGER PRIMARY KEY NOT NULL,
    episode_id INTEGER FOREIGN KEY NOT NULL,
    quotee_id INTEGER FOREIGN KEY NOT NULL,
    timestamp_start TEXT,
    timestamp_end TEXT,
    sreenshot_timestamp TEXT,
    screenshot TEXT --link to img
    is_favorite BOOLEAN

)

