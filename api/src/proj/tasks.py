from typing import Dict, List
from sqlalchemy.orm import Session
from player.models.player import Pitches
from player.schemas.pitches_schemas import PitchesCreate
from .celery import app
import statsapi
from celery import Task
from db.database import SessionLocal

class RetrievePitchesTask(Task):
    def on_success(self, retval, task_id, args, kwargs) -> None:
        pitches_create = PitchesCreate(
            season=args[2],
            team_id=args[1],
            pitches=retval
        )

        create_pitches(SessionLocal(), pitches_create, args[0])

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


@app.task(base=RetrievePitchesTask)
def request_pitches_for_year(mlb_id:int, team_id:int, year:int) -> List[Dict[str, str | int]]:
    team_schedule = statsapi.schedule(team=team_id, start_date=str(year) + "-01-01", end_date=str(year) + "-12-31")
    pitch_types = {}
    pitch_list = []

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

    return pitch_list
