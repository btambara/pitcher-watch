from pydantic import BaseModel


class PitchesBase(BaseModel):
    season: int
    team_id: int
    pitches: list[dict]


class PitchesCreate(PitchesBase):
    pass


class PitchesUpdate(PitchesBase):
    pass


class Pitches(PitchesBase):
    id: int
    mlb_id: int

    class Config:
        from_attributes = True
