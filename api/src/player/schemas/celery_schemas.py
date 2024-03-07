from pydantic import BaseModel


class CeleryTasksBase(BaseModel):
    pass


class CeleryTasks(CeleryTasksBase):
    id: str

    class Config:
        from_attributes = True
