from player.models import player
from settings.config import get_settings
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker


def get_session_local() -> Session:
    settings = get_settings()

    SQLALCHEMY_DATABASE_URL = settings.sqlalchemy_database_url

    engine = create_engine(SQLALCHEMY_DATABASE_URL)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    player.Base.metadata.create_all(bind=engine)

    return SessionLocal()


def get_session_test_local() -> Session:
    engine = create_engine(
        "sqlite:///test.db", connect_args={"check_same_thread": False}
    )

    SessionTestLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    player.Base.metadata.create_all(bind=engine)

    return SessionTestLocal()
