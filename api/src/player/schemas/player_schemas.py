from pydantic import BaseModel

class PlayerBase(BaseModel):
    mlb_id: int
    full_name: str
    primary_number: int


class PlayerCreate(PlayerBase):
    pass


class PlayerUpdate(PlayerBase):
    pass


class Player(PlayerBase):
    id: int

    class Config:
        orm_mode = True
