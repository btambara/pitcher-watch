from pydantic import BaseModel
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Token(BaseModel):  # type: ignore[misc]
    access_token: str
    token_type: str


class TokenData(BaseModel):  # type: ignore[misc]
    username: str
