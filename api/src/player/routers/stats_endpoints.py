from typing import List

from api.deps import get_db
from fastapi import APIRouter, Depends, HTTPException
from player.crud import stats_crud
from player.models.player import Stats
from player.schemas import stats_schemas
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/{mlb_id}", response_model=stats_schemas.Stats)
async def create_stats(
    *,
    db: Session = Depends(get_db),
    mlb_id: int,
    stats: stats_schemas.StatsCreate,
) -> Stats:
    """
    Create new stats for a player.
    """
    stats = stats_crud.create_stats(db=db, stats=stats, mlb_id=mlb_id)
    return stats


@router.get("/{id}", response_model=stats_schemas.Stats)
async def read_stats(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Stats:
    """
    Get stats by ID.
    """
    stats = stats_crud.get_stats(db=db, id=id)
    if not stats:
        raise HTTPException(status_code=404, detail="Stats not found.")
    return stats


@router.put("/{id}", response_model=stats_schemas.Stats)
async def update_stats(
    *,
    db: Session = Depends(get_db),
    id: int,
    stats_in: stats_schemas.StatsUpdate,
) -> Stats:
    """
    Update stats by ID.
    """
    stats = stats_crud.get_stats(db=db, id=id)
    if not stats:
        raise HTTPException(status_code=404, detail="Stats not found.")
    stats = stats_crud.update_stats(db=db, id=id, stats_in=stats_in)
    return stats


@router.delete("/{id}", response_model=stats_schemas.Stats)
async def delete_stats(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Stats:
    """
    Delete stats by ID.
    """
    stats = stats_crud.get_stats(db=db, id=id)
    if not stats:
        raise HTTPException(status_code=404, detail="Stats not found.")
    stats = stats_crud.remove_stats(db=db, id=id)
    return stats


@router.get("/all/{mlb_id}", response_model=list[stats_schemas.Stats])
async def read_all_stats_by_mlb_id(
    *,
    db: Session = Depends(get_db),
    mlb_id: int,
    skip: int = 0,
    limit: int | None = None,
) -> List[Stats]:
    """
    Get stats for player.
    """
    return stats_crud.get_player_stats(db=db, mlb_id=mlb_id, skip=skip, limit=limit)
