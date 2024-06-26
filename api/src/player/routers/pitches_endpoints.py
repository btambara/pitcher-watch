from typing import Annotated, Dict, List, Optional, Union

from api.deps import get_db
from fastapi import APIRouter, Depends, HTTPException
from player.crud import pitches_crud
from player.models.player import Pitches, PitchType
from player.schemas import pitches_schemas
from security.helpers import get_current_user
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/{mlb_id}", response_model=pitches_schemas.Pitches)  # type: ignore[misc]
async def create_pitches(
    *,
    db: Session = Depends(get_db),
    mlb_id: int,
    pitches: pitches_schemas.PitchesCreate,
) -> Optional[Pitches]:
    """
    Create new set of pitches for a player.
    """
    pitches_created = pitches_crud.create_pitches(db=db, pitches=pitches, mlb_id=mlb_id)
    return pitches_created


@router.get("/{id}", response_model=pitches_schemas.Pitches)  # type: ignore[misc]
async def read_pitches(
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


@router.put("/{id}", response_model=pitches_schemas.Pitches)  # type: ignore[misc]
async def update_pitches(
    *,
    token: Annotated[str, Depends(get_current_user)],
    db: Session = Depends(get_db),
    id: int,
    pitches_in: pitches_schemas.PitchesUpdate,
) -> Optional[Pitches]:
    """
    Update pitches by ID.
    """
    pitches = pitches_crud.get_pitches(db=db, id=id)
    if not pitches:
        raise HTTPException(status_code=404, detail="Pitches not found.")
    pitches = pitches_crud.update_pitches(db=db, id=id, pitches_in=pitches_in)
    return pitches


@router.delete("/{id}", response_model=pitches_schemas.Pitches)  # type: ignore[misc]
async def delete_pitches(
    *,
    token: Annotated[str, Depends(get_current_user)],
    db: Session = Depends(get_db),
    id: int,
) -> Optional[Pitches]:
    """
    Delete pitches by ID.
    """
    pitches = pitches_crud.get_pitches(db=db, id=id)
    if not pitches:
        raise HTTPException(status_code=404, detail="Pitches not found.")
    pitches = pitches_crud.remove_pitches(db=db, id=id)
    return pitches


@router.get(  # type: ignore[misc]
    "/all/{mlb_id}",
    response_model=Union[List[pitches_schemas.Pitches], List[Dict[str, str]]],
)
async def read_all_pitches_by_mlb_id(
    *,
    db: Session = Depends(get_db),
    mlb_id: int,
    skip: int = 0,
    limit: int = 100,
) -> Union[List[Pitches], List[Dict[str, str]]]:
    """
    Get pitches for player or returns a list of celery task IDs.
    """
    return pitches_crud.get_player_pitches(db=db, mlb_id=mlb_id, skip=skip, limit=limit)


@router.post("/pitch_type/{id}", response_model=pitches_schemas.PitchType)  # type: ignore[misc]
async def create_pitch_type(
    *,
    db: Session = Depends(get_db),
    id: int,
    pitch_type: pitches_schemas.PitchTypeCreate,
) -> (
    PitchType
):  # pragma: no cover (This is only called when we call read_all_pitches_by_mlb_id)
    """
    Create a pitch type.
    """
    pitch_type_created = pitches_crud.create_pitch_type(
        db=db, pitch_type=pitch_type, pitches_id=id
    )
    return pitch_type_created


@router.get("/pitch_type/{id}", response_model=pitches_schemas.PitchType)  # type: ignore[misc]
async def read_pitch_types(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> (
    Pitches
):  # pragma: no cover (This is only called when we call read_all_pitches_by_mlb_id)
    """
    Get pitch types by ID.
    """
    pitches = pitches_crud.get_pitch_type(db=db, id=id)
    if not pitches:
        raise HTTPException(status_code=404, detail="Pitch type not found.")
    return pitches
