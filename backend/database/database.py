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


conn.commit()
