from celery.result import AsyncResult
from proj.celery import app
from sqlalchemy.orm import Session


def is_celery_task_finished(
    db: Session, id: str
) -> bool:  # pragma: no cover (unable to test celery)
    if AsyncResult(id=id, app=app).state != "SUCCESS":
        return False
    return True
