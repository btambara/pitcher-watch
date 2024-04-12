from typing import Any, Generator

import pytest
from fastapi.testclient import TestClient
from main import app
from settings.config import get_settings, get_settings_override


@pytest.fixture  # type: ignore[misc]
def test_client() -> Generator[TestClient, Any, None]:
    app.dependency_overrides[get_settings] = get_settings_override
    client = TestClient(app)
    yield client
