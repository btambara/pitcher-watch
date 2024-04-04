from typing import Generator

from db.database import get_session_local, get_session_test_local


def get_db() -> Generator:
    db = get_session_local()
    try:
        yield db
    finally:
        db.close()


def get_test_db() -> Generator:
    db = get_session_test_local()
    try:
        yield db
    finally:
        db.close()
