from datetime import datetime

from pydantic import BaseModel, ConfigDict, constr, field_validator


class ChatCreate(BaseModel):
    title: constr(min_length=1, max_length=200)  # type: ignore

    @field_validator("title")
    @classmethod
    def validate_title(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("title cannot be empty or spaces only")
        return value


class ChatResponse(BaseModel):
    id: int
    title: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
