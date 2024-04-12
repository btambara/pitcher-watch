from pydantic import BaseModel, ConfigDict


class StatTypeBase(BaseModel):  # type:ignore[misc]
    stat: str
    value: str


class StatTypeCreate(StatTypeBase):
    pass


class StatTypeUpdate(StatTypeBase):
    pass


class StatType(StatTypeBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    stats_id: int


class StatsBase(BaseModel):  # type:ignore[misc]
    season: int
    team_id: int


class StatsCreate(StatsBase):
    pass


class StatsUpdate(StatsBase):
    pass


class Stats(StatsBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    mlb_id: int
    stats: list[StatType] = []
