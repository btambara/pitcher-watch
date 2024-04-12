from datetime import datetime

import statsapi
from player.models.player import Pitches, PitchType
from player.schemas.pitches_schemas import PitchesCreate, PitchesUpdate, PitchTypeCreate
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

        responses = []
        for season in range(from_year, to_year, 1):
            team_id = statsapi.lookup_player(mlb_id, season=season).pop()[
                "currentTeam"
            ]["id"]

            responses.append(
                {"UUID": str(request_pitches_for_year.delay(mlb_id, team_id, season))}
            )
        return responses
    pitches.sort(key=lambda x: x.season, reverse=True)
    return pitches


def create_pitches(db: Session, pitches: PitchesCreate, mlb_id: int):
    db_pitches = Pitches(
        mlb_id=mlb_id,
        season=pitches.season,
        team_id=pitches.team_id,
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


def create_pitch_type(db: Session, pitch_type: PitchTypeCreate, pitches_id: int):
    db_pitch_type = PitchType(
        pitch=pitch_type.pitch, amount=pitch_type.amount, pitches_id=pitches_id
    )

    db.add(db_pitch_type)
    db.commit()
    db.refresh(db_pitch_type)
    return db_pitch_type


def get_pitch_type(db: Session, id: int):
    return db.query(PitchType).filter(PitchType.id == id).first()


def update_pitch_type(db: Session, id: int, pitch_type_in: PitchesUpdate):
    db_pitch_type = db.query(PitchType).filter(PitchType.id == id).first()
    db_pitch_type.pitch = pitch_type_in.pitch
    db_pitch_type.amount = pitch_type_in.amount
    db_pitch_type.pitches_id = pitch_type_in.pitches_id

    db.add(db_pitch_type)
    db.commit()
    db.refresh(db_pitch_type)
    return db_pitch_type


def remove_pitch_type(db: Session, id: int):
    db_pitch_type = db.query(PitchType).filter(PitchType.id == id).first()
    db.delete(db_pitch_type)
    db.commit()
    return db_pitch_type
