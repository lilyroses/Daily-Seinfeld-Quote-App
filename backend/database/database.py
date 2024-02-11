import sqlite3

conn = sqlite3.connect('seinfeld_quote_of_the_day.db')

c = conn.cursor()

c.execute("""CREATE TABLE seasons (
    season_id int,
    season_no int,
    season_air_date_start text,
    season_air_date_end text,
    season_number_of_episodes int)""")

