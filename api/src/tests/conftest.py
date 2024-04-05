import pytest
from fastapi.testclient import TestClient
from main import app
from settings.config import get_settings, get_settings_override


@pytest.fixture
def test_client():
    app.dependency_overrides[get_settings] = get_settings_override
    client = TestClient(app)
    yield client
