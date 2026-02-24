from pydantic import BaseModel, Field, validator
from typing import Optional


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: str = Field(..., min_length=3, max_length=500)

    @validator("title")
    def title_cannot_be_blank(cls, value):
        if not value.strip():
            raise ValueError("Title cannot be empty or blank")
        return value


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = Field(None, min_length=3, max_length=500)
    completed: Optional[bool] = None

    @validator("title")
    def validate_title(cls, value):
        if value is not None and not value.strip():
            raise ValueError("Title cannot be blank")
        return value


class TaskResponse(BaseModel):
    id: str
    title: str
    description: str
    completed: bool