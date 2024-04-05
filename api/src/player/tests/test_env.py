import logging

import pytest
from fastapi.testclient import TestClient
from main import app
from settings.config import get_settings, get_settings_override


@pytest.fixture
def test_client():
    app.dependency_overrides[get_settings] = get_settings_override
    client = TestClient(app)
    yield client


def test_env(test_client) -> None:
    test_client.get("/api/v1/players/?skip=0")
    logging.getLogger(__name__).warning("Hi")
    assert 1 == 1
