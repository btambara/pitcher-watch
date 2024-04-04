from pydantic import BaseModel, ConfigDict


class StatsBase(BaseModel):
    season: int
    team_id: int
    stats: dict


class StatsCreate(StatsBase):
    pass


class StatsUpdate(StatsBase):
    pass


class Stats(StatsBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    mlb_id: int
