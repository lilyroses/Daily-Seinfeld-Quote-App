"""Update the seasons and episodes tables in database.db"""

from seasons import seasons
from database import (
    get_season_records,
    get_episode_records,
    add_records_to_seasons,
    add_records_to_episodes,
)

# Get season and episode information from seasons.py
season_records = get_season_records(seasons)
episode_records = get_episode_records(seasons)

# Update database.db with required attributes
add_records_to_seasons(season_records)
add_records_to_episodes(episode_records)
