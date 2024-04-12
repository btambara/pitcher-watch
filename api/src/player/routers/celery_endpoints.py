from typing import Dict

from api.deps import get_db
from fastapi import APIRouter, Depends
from player.crud import celery_crud
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=Dict[str, bool])
async def check_celery_task(
    *,
    db: Session = Depends(get_db),
    id: str,
) -> Dict[str, bool]:
    """
    Checks if the celery task have a status of SUCCESS.
    """
    tasks_successful = celery_crud.is_celery_task_finished(db=db, id=id)
    return {"result": tasks_successful}
