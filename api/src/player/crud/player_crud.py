from typing import List, Optional

import statsapi
from player.models.player import Player
from player.schemas.player_schemas import PlayerCreate, PlayerUpdate
from settings.config import get_settings
from sqlalchemy.orm import Session

settings = get_settings()


def get_player(db: Session, id: int) -> Optional[Player]:
    return db.query(Player).filter(Player.id == id).first()  # type: ignore[no-any-return]


def get_all_players(
    db: Session, position: str | None = None, skip: int = 0, limit: int = 100
) -> List[Player]:
    all_players = db.query(Player).offset(skip).limit(limit).all()

    if len(all_players) == 0 and settings.environment != "TEST":
        for team in statsapi.get("teams", {"sportId": 1})[
            "teams"
        ]:  # pragma: no cover (This will call MLB api, so for now I'm not testing this)
            for player in statsapi.get(
                "team_roster", {"teamId": team["id"], "rosterType": "40Man"}
            )["roster"]:
                primary_number = (
                    player["jerseyNumber"] if player["jerseyNumber"] != "" else -1
                )
                if (
                    "fullName" in player["person"]
                    and get_player_by_mlb_id(db, player["person"]["id"]) is None
                ):
                    player_create = PlayerCreate(
                        mlb_id=player["person"]["id"],
                        full_name=player["person"]["fullName"],
                        primary_number=primary_number,
                        primary_position_code=player["position"]["code"],
                        current_team_id=player["parentTeamId"],
                    )
                    create_player(db, player_create)

        all_players = (
            db.query(Player).offset(skip).limit(limit).all()
        )  # pragma: no cover (This will call MLB api, so for now I'm not testing this)

    if not position:
        return all_players  # type: ignore[no-any-return]
    else:
        return (  # type: ignore[no-any-return]
            db.query(Player)
            .filter(Player.primary_position_code == position)
            .offset(skip)
            .limit(limit)
            .all()
        )


def get_player_by_mlb_id(db: Session, mlb_id: int) -> Optional[Player]:
    return db.query(Player).filter(Player.mlb_id == mlb_id).first()  # type: ignore[no-any-return]


def get_player_by_full_name(db: Session, full_name: str) -> Optional[Player]:
    return db.query(Player).filter(Player.full_name == full_name).first()  # type: ignore[no-any-return]


def get_player_by_primary_number(db: Session, primary_number: int) -> Optional[Player]:
    return db.query(Player).filter(Player.primary_number == primary_number).first()  # type: ignore[no-any-return]


def create_player(db: Session, player: PlayerCreate) -> Player:
    db_player = Player(
        mlb_id=player.mlb_id,
        full_name=player.full_name,
        primary_number=player.primary_number,
        current_team_id=player.current_team_id,
        primary_position_code=player.primary_position_code,
    )

    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player


def remove_player(db: Session, id: int) -> Optional[Player]:
    db_player = db.query(Player).filter(Player.id == id).first()
    db.delete(db_player)
    db.commit()
    return db_player  # type: ignore[no-any-return]


def update_player(db: Session, id: int, player_in: PlayerUpdate) -> Optional[Player]:
    db_player = db.query(Player).filter(Player.id == id).first()
    db_player.mlb_id = player_in.mlb_id
    db_player.full_name = player_in.full_name
    db_player.primary_number = player_in.primary_number

    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player  # type: ignore[no-any-return]
