import logging

import pytest
from api.deps import get_db, get_test_db
from fastapi.testclient import TestClient
from main import app


@pytest.fixture
def test_client():
    app.dependency_overrides[get_db] = get_test_db
    client = TestClient(app)
    yield client


def test_env(test_client) -> None:
    test_client.get("/api/v1/players/?skip=0")
    logging.getLogger(__name__).warning("Hi")
    assert 1 == 1
