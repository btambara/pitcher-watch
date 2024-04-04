from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    sqlalchemy_database_url: str = Field()
    postgres_user: str = Field()
    postgres_password: str = Field()
    environment: str = Field()


@lru_cache
def get_settings():
    return Settings()
