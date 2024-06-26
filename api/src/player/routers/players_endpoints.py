from typing import Annotated, List, Optional

from api.deps import get_db
from fastapi import APIRouter, Depends, HTTPException
from player.crud import player_crud
from player.models.player import Player
from player.schemas import player_schemas
from security.helpers import get_current_user
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=player_schemas.Player)  # type: ignore[misc]
async def create_player(
    *,
    token: Annotated[str, Depends(get_current_user)],
    db: Session = Depends(get_db),
    player: player_schemas.PlayerCreate,
) -> Player:
    """
    Create new player.
    """
    player = player_crud.create_player(db=db, player=player)
    return player


@router.get("/{id}", response_model=player_schemas.Player)  # type: ignore[misc]
async def read_player(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Player:
    """
    Get player by ID.
    """
    player = player_crud.get_player(db=db, id=id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found.")
    return player


@router.get("/name/{full_name}", response_model=player_schemas.Player)  # type: ignore[misc]
async def read_player_by_fullname(
    *,
    db: Session = Depends(get_db),
    full_name: str,
) -> Player:
    """
    Get player by player_name.
    """
    player = player_crud.get_player_by_full_name(db=db, full_name=full_name)
    if not player:
        raise HTTPException(status_code=404, detail="No player with that name.")
    return player


@router.get("/mlb/{mlb_id}", response_model=player_schemas.Player)  # type: ignore[misc]
async def read_player_by_mlb_id(
    *,
    db: Session = Depends(get_db),
    mlb_id: int,
) -> Player:
    """
    Get player by MLB id.
    """
    player = player_crud.get_player_by_mlb_id(db=db, mlb_id=mlb_id)
    if not player:
        raise HTTPException(status_code=404, detail="No player with that MLB id.")
    return player


@router.get("/number/{primary_number}", response_model=player_schemas.Player)  # type: ignore[misc]
async def read_player_by_primary_number(
    *,
    db: Session = Depends(get_db),
    primary_number: int,
) -> Player:
    """
    Get player by primary number.
    """
    player = player_crud.get_player_by_primary_number(
        db=db, primary_number=primary_number
    )
    if not player:
        raise HTTPException(status_code=404, detail="No player with that number")
    return player


@router.put("/{id}", response_model=player_schemas.Player)  # type: ignore[misc]
async def update_player(
    *,
    token: Annotated[str, Depends(get_current_user)],
    db: Session = Depends(get_db),
    id: int,
    player_in: player_schemas.PlayerUpdate,
) -> Optional[Player]:
    """
    Update an player.
    """
    player = player_crud.get_player(db=db, id=id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found.")
    player = player_crud.update_player(db=db, id=id, player_in=player_in)
    return player


@router.delete("/{id}", response_model=player_schemas.Player)  # type: ignore[misc]
async def delete_player(
    *,
    token: Annotated[str, Depends(get_current_user)],
    db: Session = Depends(get_db),
    id: int,
) -> Optional[Player]:
    """
    Delete an player.
    """
    player = player_crud.get_player(db=db, id=id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found.")
    player = player_crud.remove_player(db=db, id=id)
    return player


@router.get("/", response_model=list[player_schemas.Player])  # type: ignore[misc]
async def read_all_players(
    *,
    db: Session = Depends(get_db),
    position: str | None = None,
) -> List[Player]:
    """
    Get all players.
    """
    return player_crud.get_all_players(db=db, position=position)
