from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):  # type:ignore[misc]
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    sqlalchemy_database_url: str = Field()
    postgres_user: str = Field()
    postgres_password: str = Field()
    environment: str = Field()

    secret_key: str = Field()
    access_token_expire_minutes: int = Field()


@lru_cache
def get_settings() -> Settings:
    return Settings()


@lru_cache
def get_settings_override() -> Settings:
    return Settings(sqlalchemy_database_url="sqlite:///test.db", environment="TEST")
