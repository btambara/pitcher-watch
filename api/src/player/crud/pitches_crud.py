from datetime import datetime

import statsapi
from player.models.player import Pitches
from player.schemas.pitches_schemas import PitchesCreate, PitchesUpdate
from proj.tasks import request_pitches_for_year
from sqlalchemy.orm import Session


def get_pitches(db: Session, id: int):
    return db.query(Pitches).filter(Pitches.id == id).first()


def get_player_pitches(
    db: Session, mlb_id: int | None = None, skip: int = 0, limit: int = 100
):
    pitches = (
        db.query(Pitches)
        .filter(Pitches.mlb_id == mlb_id)
        .offset(skip)
        .limit(limit)
        .all()
    )

    if len(pitches) == 0:
        season_start = statsapi.latest_season()["regularSeasonStartDate"]
        season_start_date = datetime.strptime(season_start, "%Y-%m-%d").date()
        today_date = datetime.now().date()

        if (season_start_date - today_date).days <= 0:
            to_year = datetime.now().year + 1
        else:
            to_year = datetime.now().year

        player_stat_data = statsapi.player_stat_data(mlb_id)
        mlb_debut_datetime = datetime.strptime(
            player_stat_data["mlb_debut"], "%Y-%m-%d"
        )
        from_year = mlb_debut_datetime.year

        team_id = statsapi.lookup_team(player_stat_data["current_team"])[0]["id"]

        responses = []
        for year in range(from_year, to_year, 1):
            responses.append(
                {"UUID": str(request_pitches_for_year.delay(mlb_id, team_id, year))}
            )
        return responses
        # pitches_create = PitchesCreate(
        #     season=year,
        #     team_id=-1,
        #     pitches=pitch_list
        # )

        # create_pitches(Depends(get_db), pitches_create, mlb_id)

    return pitches


def create_pitches(db: Session, pitches: PitchesCreate, mlb_id: int):
    db_pitches = Pitches(
        mlb_id=mlb_id,
        season=pitches.season,
        team_id=pitches.team_id,
        pitches=pitches.pitches,
    )

    db.add(db_pitches)
    db.commit()
    db.refresh(db_pitches)
    return db_pitches


def remove_pitches(db: Session, id: int):
    db_pitches = db.query(Pitches).filter(Pitches.id == id).first()
    db.delete(db_pitches)
    db.commit()
    return db_pitches


def update_pitches(db: Session, id: int, pitches_in: PitchesUpdate):
    db_pitches = db.query(Pitches).filter(Pitches.id == id).first()
    db_pitches.mlb_id = pitches_in.mlb_id
    db_pitches.season = pitches_in.season
    db_pitches.team_id = pitches_in.team_id
    db.db_pitches.stats = pitches_in.pitches

    db.add(db_pitches)
    db.commit()
    db.refresh(db_pitches)
    return db_pitches
