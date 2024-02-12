"""Update the tables in database.db"""

from seasons import seasons
from database import (
    get_season_records,
    get_episode_records,
    get_quote
    add_records_to_seasons,
    add_records_to_episodes,
)

# CREATE TABLE RECORDS
# Season records
season_records = get_season_records(seasons)
# Episode records
episode_records = get_episode_records(seasons)

# WRITE RECORDS TO TABLE
# Write seasons records
add_records_to_seasons(season_records)
# Write episodes records
add_records_to_episodes(episode_records)
