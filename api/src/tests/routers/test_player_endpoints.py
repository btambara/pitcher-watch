import random

from auth_token.token_model import Token
from fastapi.testclient import TestClient

random_mlb_id = random.randint(100000, 999999)

test_player = {
    "mlb_id": random_mlb_id,
    "full_name": "Test Player",
    "primary_number": 5,
    "current_team_id": 0,
    "primary_position_code": "P",
}


def test_create_player_endpoint(
    get_test_user_token: Token, test_client: TestClient
) -> None:
    response = test_client.post(
        "/api/v1/players/",
        json=test_player,
        headers={"Authorization": f"Bearer {get_test_user_token.access_token}"},
    )

    assert response.status_code == 200

    response_json = response.json()
    assert response_json["mlb_id"] == test_player["mlb_id"]
    assert response_json["full_name"] == test_player["full_name"]
    assert response_json["primary_number"] == test_player["primary_number"]
    assert response_json["current_team_id"] == test_player["current_team_id"]
    assert (
        response_json["primary_position_code"] == test_player["primary_position_code"]
    )
    assert response_json["stats"] == []


def test_get_player_by_mlb_id_endpoint(test_client: TestClient) -> None:
    response = test_client.get("/api/v1/players/mlb/" + str(random_mlb_id))

    assert response.status_code == 200

    response_json = response.json()
    assert response_json["mlb_id"] == test_player["mlb_id"]
    assert response_json["full_name"] == test_player["full_name"]
    assert response_json["primary_number"] == test_player["primary_number"]
    assert response_json["current_team_id"] == test_player["current_team_id"]
    assert (
        response_json["primary_position_code"] == test_player["primary_position_code"]
    )
    assert response_json["stats"] == []


def test_get_player_by_full_name_endpoint(test_client: TestClient) -> None:
    response = test_client.get("/api/v1/players/name/" + str(test_player["full_name"]))

    assert response.status_code == 200

    response_json = response.json()
    assert response_json["mlb_id"] == test_player["mlb_id"]
    assert response_json["full_name"] == test_player["full_name"]
    assert response_json["primary_number"] == test_player["primary_number"]
    assert response_json["current_team_id"] == test_player["current_team_id"]
    assert (
        response_json["primary_position_code"] == test_player["primary_position_code"]
    )
    assert response_json["stats"] == []


def test_get_player_by_primary_number_endpoint(test_client: TestClient) -> None:
    response = test_client.get(
        "/api/v1/players/number/" + str(test_player["primary_number"])
    )

    assert response.status_code == 200

    response_json = response.json()
    assert response_json["mlb_id"] == test_player["mlb_id"]
    assert response_json["full_name"] == test_player["full_name"]
    assert response_json["primary_number"] == test_player["primary_number"]
    assert response_json["current_team_id"] == test_player["current_team_id"]
    assert (
        response_json["primary_position_code"] == test_player["primary_position_code"]
    )
    assert response_json["stats"] == []


def test_update_player_endpoint(
    get_test_user_token: Token, test_client: TestClient
) -> None:
    update_test_player = test_player.copy()
    update_test_player["full_name"] = "New Test Name"

    response = test_client.put(
        "/api/v1/players/1",
        json=update_test_player,
        headers={"Authorization": f"Bearer {get_test_user_token.access_token}"},
    )

    assert response.status_code == 200

    response_json = response.json()
    assert response_json["mlb_id"] == update_test_player["mlb_id"]
    assert response_json["full_name"] == update_test_player["full_name"]
    assert response_json["primary_number"] == update_test_player["primary_number"]
    assert response_json["current_team_id"] == update_test_player["current_team_id"]
    assert (
        response_json["primary_position_code"]
        == update_test_player["primary_position_code"]
    )
    assert response_json["stats"] == []


def test_delete_player_endpoint(
    get_test_user_token: Token, test_client: TestClient
) -> None:
    response = test_client.delete(
        "/api/v1/players/1",
        headers={"Authorization": f"Bearer {get_test_user_token.access_token}"},
    )

    assert response.status_code == 200
