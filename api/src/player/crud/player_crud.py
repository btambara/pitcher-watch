from sqlalchemy.orm import Session

from player.models.player import Player
from player.schemas.player_schemas import PlayerCreate, PlayerUpdate


def get_player(db: Session, id: int):
    return db.query(Player).filter(Player.id == id).first()

def get_all_players(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Player).offset(skip).limit(limit).all()

def get_player_by_mlb_id(db: Session, mlb_id: int):
    return db.query(Player).filter(Player.mlb_id == mlb_id).first()

def get_player_by_full_name(db: Session, full_name: str):
    return db.query(Player).filter(Player.full_name == full_name).first()

def get_player_by_primary_number(db: Session, primary_number: int):
    return db.query(Player).filter(Player.primary_number == primary_number).first()

def create_player(db: Session, player: PlayerCreate):
    db_player = Player(
        mlb_id=player.mlb_id,
        full_name=player.full_name,
        primary_number=player.primary_number,
    )
    
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player


def remove_player(db: Session, id: int):
    db_player = db.query(Player).filter(Player.id == id).first()
    db.delete(db_player)
    db.commit()
    return db_player


def update_player(db: Session, id: int, player_in: PlayerUpdate):
    db_player = db.query(Player).filter(Player.id == id).first()
    db_player.mlb_id = player_in.mlb_id
    db_player.full_name = player_in.full_name
    db_player.primary_number = player_in.primary_number

    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player
