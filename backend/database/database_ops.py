"""Database ops: Create records from seasons module for tables in database.db."""

import sqlite3


# Create lists of records for database tables using seasons the module
# for necessary information.


# RECORD CREATION FUNCTIONS
# Create records for the seasons table.
def create_records_seasons(seasons):
    """
    Create a list of records using information from the seasons module
    for the seasons table in database 'database.db'.

    REQUIRED VALUES FOR TABLE seasons:
        - season_id (int, PK)
        - season_no (int)
        - air_date_start (str)
        - air_date_end (str)
    """

    # Holds all season records (stored as tuples).
    records_seasons = []

    # Get the 4 required attributes from the seasons dicts.
    for season in seasons:
        season_id = int(season["season_id"])
        season_no = int(season["season_no"])
        # List of one to two years the season ran.
        air_date_start = season["air_dates"][0]
        air_date_end = season["air_dates"][-1]
        # Create a record (tuple) for a single season.
        record = (season_id, season_no, air_date_start, air_date_end)
        # Add the record to the list of all season records.
        records_seasons.append(record)
    # Return a list of tuples for using with the `add_records_to_seasons()`
    # function, which uses sqlite3 builtin executemany().
    return records_seasons


# Create records for the episodes table.
def create_records_episodes(seasons):
    """
    Create a list of records (tuples) using information from the seasons
    module for the episodes table in database 'database.db'.

    REQUIRED VALUES FOR TABLE episodes:
        - episode_id (int, PK)
        - season_id (int, FK)
        - episode_no (int)
        - chronological_no (int)
        - title (str)
        - air_date (str)
    """
    # Holds all episode records (stored as tuples).
    records_episodes = []

    # Get the 6 required attributes from the seasons dicts.
    for season in seasons:
        # Season id is the linking FK.
        season_id = season["season_id"]
        # Get the rest of the attributes.
        for episode in season["episodes"]:
            episode_id = int(episode["episode_id"])
            episode_no = int(episode["episode_no"])
            chronological_no = int(episode["chronological_no"])
            title = episode["title"]
            air_date = episode["air_date"]
            # Create a record (tuple) for a single episode.
            record = (
                episode_id,
                season_id,
                episode_no,
                chronological_no,
                title,
                air_date,
            )
            # Add the record to the list of all episode records.
            records_episodes.append(record)
    # Return a list of tuples for using with the `add_records_to_seasons()`
    # function, which uses sqlite3 builtin executemany().
    return records_episodes


# Create records for the quotes table.
def create_records_quotes(quotes):
    """
    Create a list of records using information from the seasons module
    for the quotes table in database 'database.db'.

    REQUIRED VALUES FOR TABLE quotes:
        - quote_id (int, PK)
        - quotee_id (int, FK)
        - episode_id (int, FK) (is this necessary with quotee_id?)
    """

    # Holds all quotes records (stored as tuples).
    records_quotes = []

    # Get the required attributes from the seasons dicts.
    record = ()
    records_quotes.append(record)

    # Return a list of tuples for using with the `add_records_to_seasons()`
    # function, which uses sqlite3 builtin executemany().
    return records_quotes


# Create records for the quotees table.
def create_records_quotees(quotes):
    # Implement kword args!
    pass


# Create records for the characters table.
def create_records_characters(quotes):
    # Implement kword args!
    pass


# WRITE FUNCTIONS
# Write records to the seasons table.
def write_records_seasons(records_seasons):
    """Write the created records to table seasons in database.db"""
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    # Add values to table
    c.executemany(
        """INSERT INTO seasons VALUES
                  (?,?,?,?)""",
        (season_records),
    )
    # Write records to the seasons table in database.db
    conn.commit()


# Write records to the episodes table.
def write_records_episodes(records_episodes):
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


# Write records to the quotes table.
def write_records_quotes(records_quotes):
    pass


# Write records to the quotees table.
def write_records_quotees(records_quotees):
    pass


# Write records to the characters table
def write_records_characters(records_characters):
    pass
