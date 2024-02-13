-- Delete tables

-- DROP TABLE IF EXISTS seasons;
-- DROP TABLE IF EXISTS season;
-- DROP TABLE IF EXISTS episode;

-- CREATE TABLE IF NOT EXISTS season (
--     season_id       INTEGER PRIMARY KEY NOT NULL,
--     season_no       INTEGER NOT NULL,  -- FK for episode
--     air_date_start  TEXT    NOT NULL,
--     air_date_end    TEXT    NOT NULL,
--     total_episodes  INTEGER NOT NULL
-- );

-- CREATE TABLE IF NOT EXISTS episode (
--     episode_id          INTEGER PRIMARY KEY NOT NULL,
--     season_id           INTEGER NOT NULL,
--     episode_no          INTEGER NOT NULL,
--     chronological_no    INTEGER NOT NULL,
--     title               TEXT    NOT NULL,
--     air_date            TEXT    NOT NULL,
--     -- script BLOB NOT NULL,
--     FOREIGN KEY(season_id)  REFERENCES  seasons
-- );

CREATE TABLE IF NOT EXISTS quote (
    quote_id INTEGER PRIMARY KEY,
    quotee_id INTEGER, -- FK
    episode_id INTEGER, -- FK
    screenshot_id INTEGER, -- FK
)