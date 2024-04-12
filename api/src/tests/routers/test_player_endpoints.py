import random

random_mlb_id = random.randint(100000, 999999)

test_player = {
    "mlb_id": random_mlb_id,
    "full_name": "Test Player",
    "primary_number": 5,
    "current_team_id": 0,
    "primary_position_code": "P",
}


def test_create_player_endpoint(test_client) -> None:
    response = test_client.post(
        "/api/v1/players/",
        json=test_player,
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


def test_get_player_by_mlb_id_endpoint(test_client) -> None:
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


def test_get_player_by_full_name_endpoint(test_client) -> None:
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


def test_get_player_by_primary_number_endpoint(test_client) -> None:
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
