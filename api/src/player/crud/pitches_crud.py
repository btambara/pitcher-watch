from sqlalchemy.orm import Session

from player.models.player import Pitches
from player.schemas.pitches_schemas import PitchesCreate, PitchesUpdate

import statsapi
from datetime import datetime

def get_pitches(db: Session, id: int):
    return db.query(Pitches).filter(Pitches.id == id).first()

def get_player_pitches(db: Session, mlb_id: int | None = None, skip: int = 0, limit: int = 100):
    pitches = db.query(Pitches).filter(Pitches.mlb_id == mlb_id).offset(skip).limit(limit).all()

    if len(pitches) == 0:
        season_start = statsapi.latest_season()["regularSeasonStartDate"]
        season_start_date = datetime.strptime(season_start, "%Y-%m-%d").date()
        today_date = datetime.now().date()

        if (season_start_date - today_date).days <= 0:
            to_year = datetime.now().year + 1
        else:
            to_year = datetime.now().year
        
        player_stat_data = statsapi.player_stat_data(mlb_id)
        mlb_debut_datetime = datetime.strptime(player_stat_data['mlb_debut'], "%Y-%m-%d")
        from_year = mlb_debut_datetime.year

        team_id = statsapi.lookup_team(player_stat_data["current_team"])[0]["id"]
        pitch_list = []

        for year in range(from_year, to_year, 1):
            pitches = {}
            team_schedule = statsapi.schedule(team=team_id, start_date=str(year) + "-01-01", end_date=str(year) + "-12-31")
            pitch_types = {}
            
            for game in team_schedule:
                if game["game_type"] == "R":
                    game_data = statsapi.get("game_playByPlay", {"gamePk": game["game_id"]})
                    for play in game_data["allPlays"]:
                        current_pitcher = play["matchup"]["pitcher"]["id"]
                        for event in play["playEvents"]:
                            if "eventType" in event["details"] and event["details"]["eventType"] == "pitching_substitution":
                                current_pitcher = event["player"]["id"]
                            elif current_pitcher ==  mlb_id and event["isPitch"] and "type" in event["details"]:
                                pitch_type = event["details"]["type"]["code"]
                                
                                if pitch_type not in pitch_types:
                                    pitch_types[pitch_type] = 1
                                else:
                                    pitch_types[pitch_type] = pitch_types[pitch_type] + 1

            for pitch in pitch_types:
                pitch_list.append({
                    "code": pitch,
                    "amount": pitch_types[pitch]
                })
            
            pitches_create = PitchesCreate(
                    season=year,
                    team_id=-1,
                    pitches=pitch_list
            )
            
            create_pitches(db, pitches_create, mlb_id)

        pitches = db.query(Pitches).filter(Pitches.mlb_id == mlb_id).offset(skip).limit(limit).all()

    return pitches

def create_pitches(db: Session, pitches: PitchesCreate, mlb_id: int):
    db_pitches = Pitches(
        mlb_id=mlb_id,
        season=pitches.season,
        team_id=pitches.team_id,
        pitches=pitches.pitches

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
