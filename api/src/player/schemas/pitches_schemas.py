from pydantic import BaseModel, ConfigDict


class PitchTypeBase(BaseModel):  # type:ignore[misc]
    pitch: str
    amount: int


class PitchTypeCreate(PitchTypeBase):
    pass


class PitchTypeUpdate(PitchTypeBase):
    pass


class PitchType(PitchTypeBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    pitches_id: int


class PitchesBase(BaseModel):  # type:ignore[misc]
    season: int
    team_id: int


class PitchesCreate(PitchesBase):
    pass


class PitchesUpdate(PitchesBase):
    pass


class Pitches(PitchesBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    mlb_id: int
    pitches: list[PitchType] = []
