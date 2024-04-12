from typing import Annotated

from fastapi import Depends
from player.models import player
from settings.config import Settings, get_settings
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool


def get_session_local(settings: Annotated[Settings, Depends(get_settings)]) -> Session:
    SQLALCHEMY_DATABASE_URL = settings.sqlalchemy_database_url

    if SQLALCHEMY_DATABASE_URL.lower().startswith("sqlite:///"):
        engine = create_engine(
            SQLALCHEMY_DATABASE_URL,
            connect_args={"check_same_thread": False},
            poolclass=StaticPool,
        )
    else:
        engine = create_engine(SQLALCHEMY_DATABASE_URL)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    player.Base.metadata.create_all(bind=engine)

    return SessionLocal()
