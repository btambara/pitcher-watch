from typing import Dict, List, Union

from api.deps import get_db
from fastapi import APIRouter, Depends, HTTPException
from player.crud import pitches_crud
from player.models.player import Pitches
from player.schemas import pitches_schemas
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/{mlb_id}", response_model=pitches_schemas.Pitches)
def create_pitches(
    *,
    db: Session = Depends(get_db),
    mlb_id: int,
    pitches: pitches_schemas.PitchesCreate,
) -> Pitches:
    """
    Create new set of pitches for a player.
    """
    pitches_created = pitches_crud.create_pitches(db=db, pitches=pitches, mlb_id=mlb_id)
    return pitches_created


@router.get("/{id}", response_model=pitches_schemas.Pitches)
def read_pitches(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Pitches:
    """
    Get pitches by ID.
    """
    pitches = pitches_crud.get_pitches(db=db, id=id)
    if not pitches:
        raise HTTPException(status_code=404, detail="Pitches not found.")
    return pitches


@router.put("/{id}", response_model=pitches_schemas.Pitches)
def update_pitches(
    *,
    db: Session = Depends(get_db),
    id: int,
    pitches_in: pitches_schemas.PitchesUpdate,
) -> Pitches:
    """
    Update pitches by ID.
    """
    pitches = pitches_crud.get_pitches(db=db, id=id)
    if not pitches:
        raise HTTPException(status_code=404, detail="Pitches not found.")
    pitches = pitches_crud.update_pitches(db=db, id=id, pitches_in=pitches_in)
    return pitches


@router.delete("/{id}", response_model=pitches_schemas.Pitches)
def delete_pitches(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Pitches:
    """
    Delete pitches by ID.
    """
    pitches = pitches_crud.get_pitches(db=db, id=id)
    if not pitches:
        raise HTTPException(status_code=404, detail="Pitches not found.")
    pitches = pitches_crud.remove_pitches(db=db, id=id)
    return pitches


@router.get(
    "/all/{mlb_id}",
    response_model=Union[List[pitches_schemas.Pitches], List[Dict[str, str]]],
)
def read_all_pitches_by_mlb_id(
    *,
    db: Session = Depends(get_db),
    mlb_id: int,
    skip: int = 0,
    limit: int | None = None,
) -> Union[List[Pitches], List[Dict[str, str]]]:
    """
    Get pitches for player or returns a list of celery task IDs.
    """
    return pitches_crud.get_player_pitches(db=db, mlb_id=mlb_id, skip=skip, limit=limit)
