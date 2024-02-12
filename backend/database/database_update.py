"""Update the tables in database.db"""

from seasons import seasons
from quotes import quotes
from database_ops import (
    create_records_seasons,
    create_records_episodes,
    create_records_quotes,
    create_records_quotees,
    create_records_characters,
    write_records_seasons,
    write_records_episodes,
    write_records_quotes,
    write_records_quotees,
    write_records_characters,
)

# CREATE TABLE RECORDS
# Season records
records_seasons = create_records_seasons(seasons)
# Episode records
records_episodes = create_records_episodes(seasons)
# Quotes records
records_quotes = create_records_quotes(quotes)
# Quotees records
records_quotees = create_records_quotees(quotes)
# Characters records
records_characters = create_records_characters(quotes)


# WRITE RECORDS TO TABLE
# Write seasons records
# write_records_seasons(records_seasons)

# Write episodes records
# write_records_episodes(records_episodes)
