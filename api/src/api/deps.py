from typing import Annotated, Generator

from db.database import get_session_local
from fastapi import Depends
from settings.config import Settings, get_settings


def get_db(settings: Annotated[Settings, Depends(get_settings)]) -> Generator:
    db = get_session_local(settings)
    try:
        yield db
    finally:
        db.close()
