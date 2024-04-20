from auth_token.token_model import Token
from fastapi import status
from fastapi.datastructures import Headers
from fastapi.testclient import TestClient
from security.helpers import verify_password
from user.user_crud import get_password_hash

test_user_info = {"email": "test_user_model@testing.com", "password": "password"}


def test_login_for_access_token_with_unknown_user(test_client: TestClient) -> None:
    headers = Headers({"Content-Type": "application/x-www-form-urlencoded"})
    data = {
        "grant_type": "",
        "username": "DOESNT_EXIST",
        "password": "NO_PASSWORD",
        "scope": "",
        "client_id": "",
        "client_secret": "",
    }
    response = test_client.post(
        "/api/v1/authenticate/token", data=data, headers=headers
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_create_user(test_client: TestClient) -> None:
    response = test_client.post(
        "/api/v1/authenticate/",
        json=test_user_info,
    )

    assert response.status_code == status.HTTP_200_OK
    response_json = response.json()
    assert response_json["email"] == test_user_info["email"]
    assert verify_password(test_user_info["password"], response_json["password"])


def test_get_user_by_id(test_client: TestClient) -> None:
    response = test_client.get("/api/v1/authenticate/2")

    assert response.status_code == status.HTTP_200_OK
    response_json = response.json()
    assert response_json["email"] == test_user_info["email"]
    assert verify_password(test_user_info["password"], response_json["password"])


def test_get_user_by_id_with_unknown_id(test_client: TestClient) -> None:
    response = test_client.get("/api/v1/authenticate/-1")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    response_json = response.json()
    assert response_json == {"detail": "User not found."}


def test_get_user_by_email(test_client: TestClient) -> None:
    response = test_client.get("/api/v1/authenticate/email/" + test_user_info["email"])

    assert response.status_code == status.HTTP_200_OK
    response_json = response.json()
    assert response_json["email"] == test_user_info["email"]
    assert verify_password(test_user_info["password"], response_json["password"])


def test_get_user_by_email_with_unknown_email(test_client: TestClient) -> None:
    response = test_client.get("/api/v1/authenticate/email/EMAIL_DNE@TESTING.COM")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    response_json = response.json()
    assert response_json == {"detail": "No user with that email."}


def test_update_user_by_id(get_test_user_token: Token, test_client: TestClient) -> None:
    update_test_user = test_user_info.copy()
    update_test_user["email"] = "Updated_Email@testing.com"
    update_test_user["password"] = get_password_hash(update_test_user["password"])

    response = test_client.put(
        "/api/v1/authenticate/2",
        json=update_test_user,
        headers={"Authorization": f"Bearer {get_test_user_token.access_token}"},
    )

    assert response.status_code == status.HTTP_200_OK
    response_json = response.json()
    assert response_json["email"] == update_test_user["email"]
    assert verify_password(test_user_info["password"], response_json["password"])


def test_update_user_by_id_with_unknown_id(
    get_test_user_token: Token, test_client: TestClient
) -> None:
    update_test_user = test_user_info.copy()
    update_test_user["email"] = "Updated_Email@testing.com"
    update_test_user["password"] = get_password_hash(update_test_user["password"])

    response = test_client.put(
        "/api/v1/authenticate/-1",
        json=update_test_user,
        headers={"Authorization": f"Bearer {get_test_user_token.access_token}"},
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND
    response_json = response.json()
    assert response_json == {"detail": "User not found."}


def test_delete_user_by_id(get_test_user_token: Token, test_client: TestClient) -> None:
    response = test_client.delete(
        "/api/v1/authenticate/2",
        headers={"Authorization": f"Bearer {get_test_user_token.access_token}"},
    )

    assert response.status_code == status.HTTP_200_OK


def test_delete_user_by_id_with_unknown_id(
    get_test_user_token: Token, test_client: TestClient
) -> None:
    response = test_client.delete(
        "/api/v1/authenticate/-1",
        headers={"Authorization": f"Bearer {get_test_user_token.access_token}"},
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND
