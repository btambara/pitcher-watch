from player.schemas.stats_schemas import Stats
from pydantic import BaseModel


class PlayerBase(BaseModel):
    mlb_id: int
    full_name: str
    primary_number: int
    current_team_id: int
    primary_position_code: str


class PlayerCreate(PlayerBase):
    pass


class PlayerUpdate(PlayerBase):
    pass


class Player(PlayerBase):
    id: int
    stats: list[Stats] = []

    class Config:
        from_attributes = True
