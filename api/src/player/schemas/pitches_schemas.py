from pydantic import BaseModel, ConfigDict


class PitchesBase(BaseModel):
    season: int
    team_id: int
    pitches: list[dict]


class PitchesCreate(PitchesBase):
    pass


class PitchesUpdate(PitchesBase):
    pass


class Pitches(PitchesBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    mlb_id: int
