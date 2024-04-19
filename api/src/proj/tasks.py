from typing import Dict, List

import httpx
import statsapi
from celery import Task

from .celery import app


class RetrievePitchesTask(Task):  # type: ignore[misc]
    def on_success(
        self,
        retval: List[Dict[str, str | int]],
        task_id: str,
        args: List[str],
        kwargs: Dict[str, str],
    ) -> None:
        response = httpx.post(  # pragma: no cover (Need to add functionality to test Celery task)
            "http://api:8393/api/v1/player/pitches/" + str(args[0]),
            json={"season": int(args[2]), "team_id": int(args[1])},
        )
        response_json = (
            response.json()
        )  # pragma: no cover (Need to add functionality to test Celery task)

        for (
            pitch
        ) in retval:  # pragma: no cover (Need to add functionality to test Celery task)
            response = httpx.post(
                "http://api:8393/api/v1/player/pitches/pitch_type/"
                + str(response_json["id"]),
                json={"pitch": pitch["code"], "amount": int(pitch["amount"])},
            )


@app.task(base=RetrievePitchesTask)  # type: ignore[misc]
def request_pitches_for_year(
    mlb_id: int, team_id: int, year: int
) -> List[Dict[str, str | int]]:
    team_schedule = statsapi.schedule(  # pragma: no cover (Need to add functionality to test Celery task)
        team=team_id, start_date=str(year) + "-01-01", end_date=str(year) + "-12-31"
    )
    pitch_types = {}  # pragma: no cover (Need to add functionality to test Celery task)
    pitch_list = []  # pragma: no cover (Need to add functionality to test Celery task)

    for (
        game
    ) in (
        team_schedule
    ):  # pragma: no cover (Need to add functionality to test Celery task)
        if game["game_type"] == "R":
            game_data = statsapi.get("game_playByPlay", {"gamePk": game["game_id"]})
            for play in game_data["allPlays"]:
                current_pitcher = play["matchup"]["pitcher"]["id"]
                for event in play["playEvents"]:
                    if (
                        "eventType" in event["details"]
                        and event["details"]["eventType"] == "pitching_substitution"
                    ):
                        current_pitcher = event["player"]["id"]
                    elif (
                        current_pitcher == mlb_id
                        and event["isPitch"]
                        and "type" in event["details"]
                    ):
                        pitch_type = event["details"]["type"]["code"]

                        if pitch_type not in pitch_types:
                            pitch_types[pitch_type] = 1
                        else:
                            pitch_types[pitch_type] = pitch_types[pitch_type] + 1

    for (
        pitch
    ) in (
        pitch_types
    ):  # pragma: no cover (Need to add functionality to test Celery task)
        pitch_list.append({"code": pitch, "amount": str(pitch_types[pitch])})

    return (
        pitch_list  # pragma: no cover (Need to add functionality to test Celery task)
    )
