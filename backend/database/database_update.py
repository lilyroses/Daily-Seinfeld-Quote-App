"""Update the tables in database.db"""

from seasons import seasons
from database import (
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
season_records = get_season_records(seasons)
# Episode records
episode_records = get_episode_records(seasons)

# WRITE RECORDS TO TABLE
# Write seasons records
add_records_to_seasons(season_records)
# Write episodes records
add_records_to_episodes(episode_records)
