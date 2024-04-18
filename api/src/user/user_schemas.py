from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):  # type: ignore [misc]
    email: str
    password: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
