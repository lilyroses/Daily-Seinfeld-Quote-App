import sqlite3


conn = sqlite3.connect("database.db")

c = conn.cursor()

# c.execute(
#     """CREATE TABLE seasons (
#           season_id int,
#           season_no int,
#           air_date_start text,
#           air_date_end text
#           )""")

# c.execute(
#     """CREATE TABLE episodes (
#           episode_id int,
#           season_id int,
#           episode_no int,
#           chronological_no int,
#           title text,
#           air_date text
#           )""")

# Should have been named 'quotes'; fixed below
# c.execute(
#     """CREATE TABLE quote (
#           quote_id int,
#           quotee_id int,
#           episode_id int,
#           quote_text text
#           )""")

# c.execute(
#     """CREATE TABLE quotee (
#           character_id int,
#           quote_id int,
#           image blob,
#           PRIMARY KEY (character_id, quote_id)
#           )"""
# )

# c.execute(
#     """CREATE TABLE characters (
#           character_id int,
#           name text,
#           image blob
# )"""
# )

# RENAME TABLE
c.execute(
    """ALTER TABLE quote (
    RENAME TO quotes)"""
)


# c.execute(
#     """ALTER TABLE quotes
#     ADD quote_screen_shot image,
#     ADD quote_screen_shot_timestamp text,
#     ADD quote_timestamp_start text,
#     ADD quote_timestamp_end text;"""
# )
conn.commit()
