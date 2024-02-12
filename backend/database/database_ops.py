import sqlite3
import json
from seasons import seasons


# SEASONS
def get_season_records(seasons):
    # REQUIRED VALUES FOR TABLE seasons:
    #   season_id, season_no, air_date_start,
    #   air_date_end
    # Holds all records (tuples)
    season_records = []
    # Get the 4 required attributes from the
    # seasons dicts
    for season in seasons:
        season_id = season["season_id"]
        season_no = season["season_no"]
        air_date_start = season["air_dates"][0]
        air_date_end = season["air_dates"][-1]
        # Create the record (tuple)
        record = (season_id, season_no, air_date_start, air_date_end)
        # Add the record to the list of all records
        season_records.append(record)
    # Return a list of tuples for using with c.executemany()
    # if len(season_records) == 9:
    # return season_records
    return season_records


# Add the records to the seasons table
def add_records_to_seasons(season_records):
    # Add records to the seasons table
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    # Add values to table

    c.executemany(
        """INSERT INTO seasons
                  VALUES (?,?,?,?)""",
        (season_records),
    )
    # Execute sql command
    conn.commit()


# EPISODES
def get_episode_records(seasons):
    # REQUIRED VALUES FOR TABLE episodes:
    #   episode_id, season_id, episode_no,
    #   chronological_no, title, air_date
    episode_records = []

    for season in seasons:
        # Season id is the linking FK
        season_id = season["season_id"]
        # Get the rest of the attributes
        for episode in season["episodes"]:
            episode_id = episode["episode_id"]
            episode_no = episode["episode_no"]
            chronological_no = episode["chronological_no"]
            title = episode["title"]
            air_date = episode["air_date"]
            # A tuple of all required attributes for
            # the episodes table
            record = (
                episode_id,
                season_id,
                episode_no,
                chronological_no,
                title,
                air_date,
            )
            episode_records.append(record)
    return episode_records


def add_records_to_episodes(episode_records):
    # Add records to the seasons table
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    # Add values to table
    c.executemany(
        """INSERT INTO episodes
                  VALUES (?,?,?,?,?,?)""",
        (episode_records),
    )
    # Execute sql command
    conn.commit()
