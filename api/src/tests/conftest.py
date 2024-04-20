import random
from typing import Any, Generator

import pytest
from auth_token.token_model import Token
from fastapi.testclient import TestClient
from httpx import Headers
from main import app
from player.models.player import Player
from settings.config import get_settings, get_settings_override
from user.user_model import User

test_user_info = {"email": "test@testing.com", "password": "password"}

random_mlb_id = random.randint(100000, 999999)

test_player = {
    "mlb_id": 647351,
    "full_name": "Abraham Toro",
    "primary_number": 31,
    "current_team_id": 133,
    "primary_position_code": "5",
}


@pytest.fixture  # type: ignore[misc]
def test_client() -> Generator[TestClient, Any, None]:
    app.dependency_overrides[get_settings] = get_settings_override
    client = TestClient(app)
    yield client


@pytest.fixture  # type: ignore[misc]
def get_test_user(test_client: TestClient) -> User:
    response = test_client.get("/api/v1/authenticate/email/" + test_user_info["email"])

    if response.status_code == 404:
        response = test_client.post(  # pragma: no cover
            "/api/v1/authenticate",
            json={
                "email": test_user_info["email"],
                "password": test_user_info["password"],
            },
        )

    response_json = response.json()

    return User(email=response_json["email"], password=response_json["password"])


@pytest.fixture  # type: ignore[misc]
def get_test_player(get_test_user_token: Token, test_client: TestClient) -> Player:
    response = test_client.get("/api/v1/players/mlb/" + str(test_player["mlb_id"]))
    import logging

    logging.getLogger(__name__).info(response)
    if response.status_code == 404:
        response = test_client.post(
            "/api/v1/players/",
            json=test_player,
            headers={"Authorization": f"Bearer {get_test_user_token.access_token}"},
        )

    response_json = response.json()
    return Player(
        mlb_id=response_json["mlb_id"],
        full_name=response_json["full_name"],
        primary_number=response_json["primary_number"],
        current_team_id=response_json["current_team_id"],
        primary_position_code=response_json["primary_position_code"],
    )


@pytest.fixture  # type: ignore[misc]
def get_test_user_token(get_test_user: User, test_client: TestClient) -> Token:
    headers = Headers({"Content-Type": "application/x-www-form-urlencoded"})
    data = {
        "grant_type": "",
        "username": get_test_user.email,
        "password": test_user_info["password"],
        "scope": "",
        "client_id": "",
        "client_secret": "",
    }
    response = test_client.post(
        "/api/v1/authenticate/token", data=data, headers=headers
    )
    response_json = response.json()

    return Token(
        access_token=response_json["access_token"],
        token_type=response_json["token_type"],
    )
