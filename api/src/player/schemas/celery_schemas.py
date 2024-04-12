from pydantic import BaseModel, ConfigDict


class CeleryTasksBase(BaseModel):
    pass


class CeleryTasks(CeleryTasksBase):
    model_config = ConfigDict(from_attributes=True)

    id: str
