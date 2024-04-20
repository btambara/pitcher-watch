from auth_token.token_model import Token
from fastapi import status
from fastapi.testclient import TestClient
from player.models.player import Player


def test_create_pitches_endpoint(
    get_test_player: Player, get_test_user_token: Token, test_client: TestClient
) -> None:
    test_pitches = {
        "mlb_id": get_test_player.mlb_id,
        "team_id": get_test_player.current_team_id,
        "season": 1830,
    }

    response = test_client.post(
        "/api/v1/player/pitches/" + str(get_test_player.mlb_id),
        json=test_pitches,
        headers={"Authorization": f"Bearer {get_test_user_token.access_token}"},
    )
    response_json = response.json()
    assert response.status_code == status.HTTP_200_OK

    assert response_json["mlb_id"] == test_pitches["mlb_id"]
    assert response_json["team_id"] == test_pitches["team_id"]
    assert response_json["season"] == test_pitches["season"]
    assert response_json["pitches"] == []


def test_read_all_pitches_by_mlb_id_endpoint(
    get_test_player: Player, test_client: TestClient
) -> None:
    test_pitches = {
        "mlb_id": get_test_player.mlb_id,
        "team_id": get_test_player.current_team_id,
        "season": 1830,
    }

    response = test_client.get(
        "/api/v1/player/pitches/all/" + str(get_test_player.mlb_id),
    )

    response_json = response.json()
    assert response.status_code == status.HTTP_200_OK

    assert response_json[0]["mlb_id"] == test_pitches["mlb_id"]
    assert response_json[0]["team_id"] == test_pitches["team_id"]
    assert response_json[0]["season"] == test_pitches["season"]
    assert response_json[0]["pitches"] == []


def test_read_pitches_by_id_endpoint(
    get_test_player: Player, test_client: TestClient
) -> None:
    test_pitches = {
        "mlb_id": get_test_player.mlb_id,
        "team_id": get_test_player.current_team_id,
        "season": 1830,
    }

    response = test_client.get(
        "/api/v1/player/pitches/1",
    )

    response_json = response.json()
    assert response.status_code == status.HTTP_200_OK

    assert response_json["mlb_id"] == test_pitches["mlb_id"]
    assert response_json["team_id"] == test_pitches["team_id"]
    assert response_json["season"] == test_pitches["season"]
    assert response_json["pitches"] == []


def test_read_pitches_by_id_endpoint_with_dne_id(test_client: TestClient) -> None:
    response = test_client.get(
        "/api/v1/player/pitches/-1",
    )

    response_json = response.json()
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response_json == {"detail": "Pitches not found."}


def test_update_pitches_by_id(
    get_test_user_token: Token, get_test_player: Player, test_client: TestClient
) -> None:
    update_test_pitches = {
        "mlb_id": get_test_player.mlb_id,
        "team_id": get_test_player.current_team_id,
        "season": 1831,
        "pitches": [],
    }

    response = test_client.put(
        "/api/v1/player/pitches/1",
        json=update_test_pitches,
        headers={"Authorization": f"Bearer {get_test_user_token.access_token}"},
    )

    assert response.status_code == status.HTTP_200_OK
    response_json = response.json()
    assert response_json["mlb_id"] == update_test_pitches["mlb_id"]
    assert response_json["team_id"] == update_test_pitches["team_id"]
    assert response_json["season"] == update_test_pitches["season"]
    assert response_json["pitches"] == []


def test_update_pitches_by_id_with_dne_id(
    get_test_user_token: Token, get_test_player: Player, test_client: TestClient
) -> None:
    update_test_pitches = {
        "mlb_id": get_test_player.mlb_id,
        "team_id": get_test_player.current_team_id,
        "season": 1831,
        "pitches": [],
    }

    response = test_client.put(
        "/api/v1/player/pitches/-1",
        json=update_test_pitches,
        headers={"Authorization": f"Bearer {get_test_user_token.access_token}"},
    )

    response_json = response.json()
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response_json == {"detail": "Pitches not found."}


def test_delete_stats_by_id(
    get_test_user_token: Token, test_client: TestClient
) -> None:
    response = test_client.delete(
        "/api/v1/player/pitches/1",
        headers={"Authorization": f"Bearer {get_test_user_token.access_token}"},
    )

    assert response.status_code == status.HTTP_200_OK


def test_delete_stats_by_id_with_dne_id(
    get_test_user_token: Token, test_client: TestClient
) -> None:
    response = test_client.delete(
        "/api/v1/player/pitches/-1",
        headers={"Authorization": f"Bearer {get_test_user_token.access_token}"},
    )

    response_json = response.json()
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response_json == {"detail": "Pitches not found."}
