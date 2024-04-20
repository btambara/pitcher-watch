from typing import List, Optional

import statsapi
from player.models.player import Stats, StatType
from player.schemas.stats_schemas import (
    StatsCreate,
    StatsUpdate,
    StatTypeCreate,
    StatTypeUpdate,
)
from sqlalchemy.orm import Session


def get_stats(db: Session, id: int) -> Optional[Stats]:
    return db.query(Stats).filter(Stats.id == id).first()  # type: ignore[no-any-return]


def get_player_stats(
    db: Session, mlb_id: int, skip: int = 0, limit: int = 100
) -> List[Stats]:
    player_stats = (
        db.query(Stats).filter(Stats.mlb_id == mlb_id).offset(skip).limit(limit).all()
    )

    if (
        len(player_stats) == 0
    ):  # pragma: no cover (This will call MLB api, so for now I'm not testing this)
        player_data = statsapi.player_stat_data(
            mlb_id, group="pitching", type="career"
        )["stats"]
        if player_data:
            career_stats = player_data[0]
            stats_create = StatsCreate(season=-1, team_id=-1)
            db_career_stats = create_stats(db, stats_create, mlb_id)

            for stat, value in career_stats["stats"].items():
                stat_type_create = StatTypeCreate(stat=stat, value=str(value))
                create_stat_type(db, stat_type_create, db_career_stats.id)

        year_by_year_stats = statsapi.player_stat_data(
            mlb_id, group="pitching", type="yearByYear"
        )
        for season_stats in year_by_year_stats["stats"]:
            stats_create = StatsCreate(season=season_stats["season"], team_id=-1)
            db_season_stat = create_stats(db, stats_create, mlb_id)

            for stat, value in season_stats["stats"].items():
                stat_type_create = StatTypeCreate(stat=stat, value=str(value))
                create_stat_type(db, stat_type_create, db_season_stat.id)

        player_stats = (
            db.query(Stats)
            .filter(Stats.mlb_id == mlb_id)
            .offset(skip)
            .limit(limit)
            .all()
        )
    player_stats.sort(key=lambda x: x.season, reverse=True)
    return player_stats  # type: ignore[no-any-return]


def create_stats(db: Session, stats: StatsCreate, mlb_id: int) -> Stats:
    db_stats = Stats(mlb_id=mlb_id, season=stats.season, team_id=stats.team_id)

    db.add(db_stats)
    db.commit()
    db.refresh(db_stats)
    return db_stats


def remove_stats(db: Session, id: int) -> Optional[Stats]:
    db_player = db.query(Stats).filter(Stats.id == id).first()
    db.delete(db_player)
    db.commit()
    return db_player  # type: ignore[no-any-return]


def update_stats(db: Session, id: int, stats_in: StatsUpdate) -> Optional[Stats]:
    db_stats = db.query(Stats).filter(Stats.id == id).first()
    db_stats.mlb_id = stats_in.mlb_id
    db_stats.season = stats_in.season
    db_stats.team_id = stats_in.team_id
    db_stats.stats = stats_in.stats

    db.add(db_stats)
    db.commit()
    db.refresh(db_stats)
    return db_stats  # type: ignore[no-any-return]


def create_stat_type(
    db: Session, stat_type: StatTypeCreate, stats_id: int
) -> StatType:  # pragma: no cover (This is only called when we call get_player_stats)
    db_stat_type = StatType(
        stat=stat_type.stat, value=stat_type.value, stats_id=stats_id
    )

    db.add(db_stat_type)
    db.commit()
    db.refresh(db_stat_type)
    return db_stat_type


def remove_stat_type(
    db: Session, id: int
) -> Optional[
    StatType
]:  # pragma: no cover (This is only called when we call get_player_stats)
    db_stat_type = db.query(Stats).filter(StatType.id == id).first()
    db.delete(db_stat_type)
    db.commit()
    return db_stat_type  # type: ignore[no-any-return]


def update_stat_type(
    db: Session, id: int, stat_type_in: StatTypeUpdate
) -> Optional[
    StatType
]:  # pragma: no cover (This is only called when we call get_player_stats)
    db_stat_type = db.query(Stats).filter(Stats.id == id).first()
    db_stat_type.stat = stat_type_in.stat
    db_stat_type.value = stat_type_in.value
    db_stat_type.stats_id = stat_type_in.stats_id

    db.add(db_stat_type)
    db.commit()
    db.refresh(db_stat_type)
    return db_stat_type  # type: ignore[no-any-return]
