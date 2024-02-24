from sqlalchemy.orm import Session

from player.models.player import Stats
from player.schemas.stats_schemas import StatsCreate, StatsUpdate

import statsapi

def get_stats(db: Session, id: int):
    return db.query(Stats).filter(Stats.id == id).first()

def get_player_stats(db: Session, mlb_id: int | None = None, skip: int = 0, limit: int = 100):
    player_stats = db.query(Stats).filter(Stats.mlb_id == mlb_id).offset(skip).limit(limit).all()

    if len(player_stats) == 0:
        career_stats = statsapi.player_stat_data(mlb_id, group="pitching", type="career")["stats"][0]
        stats_create = StatsCreate(
            season=-1,
            team_id=-1,
            stats=career_stats["stats"]
        )
        create_stats(db, stats_create, mlb_id)

        year_by_year_stats = statsapi.player_stat_data(mlb_id, group="pitching", type="yearByYear")
        for season_stats in year_by_year_stats["stats"]:
            stats_create = StatsCreate(
                season=season_stats["season"],
                team_id=-1,
                stats=season_stats["stats"]
            )
            create_stats(db, stats_create, mlb_id)
        
        player_stats = db.query(Stats).filter(Stats.mlb_id == mlb_id).offset(skip).limit(limit).all().sort(key="season", reverse=True)

    return player_stats

def create_stats(db: Session, stats: StatsCreate, mlb_id: int):
    db_stats = Stats(
        mlb_id=mlb_id,
        season=stats.season,
        team_id=stats.team_id,
        stats=stats.stats

    )
    
    db.add(db_stats)
    db.commit()
    db.refresh(db_stats)
    return db_stats


def remove_stats(db: Session, id: int):
    db_player = db.query(Stats).filter(Stats.id == id).first()
    db.delete(db_player)
    db.commit()
    return db_player


def update_stats(db: Session, id: int, stats_in: StatsUpdate):
    db_stats = db.query(Stats).filter(Stats.id == id).first()
    db_stats.mlb_id = stats_in.mlb_id
    db_stats.season = stats_in.season
    db_stats.team_id = stats_in.team_id
    db.stats.stats = stats_in.stats

    db.add(db_stats)
    db.commit()
    db.refresh(db_stats)
    return db_stats
