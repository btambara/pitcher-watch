import logging


def test_env(test_client) -> None:
    test_client.get("/api/v1/players/?skip=0")
    logging.getLogger(__name__).warning("Hi")
    assert 1 == 1
