from pydantic import BaseModel


class StatsBase(BaseModel):
    season: int
    team_id: int
    stats: dict


class StatsCreate(StatsBase):
    pass


class StatsUpdate(StatsBase):
    pass


class Stats(StatsBase):
    id: int
    mlb_id: int

    class Config:
        from_attributes = True
