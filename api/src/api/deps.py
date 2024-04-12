from typing import Annotated, Any, Generator

from db.database import get_session_local
from fastapi import Depends
from settings.config import Settings, get_settings
from sqlalchemy.orm import Session


def get_db(
    settings: Annotated[Settings, Depends(get_settings)]
) -> Generator[Session, Any, None]:
    db = get_session_local(settings)
    try:
        yield db
    finally:
        db.close()
