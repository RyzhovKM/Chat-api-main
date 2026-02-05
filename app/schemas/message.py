from datetime import datetime

from pydantic import BaseModel, ConfigDict, constr, field_validator


class MessageCreate(BaseModel):
    text: constr(min_length=1, max_length=5000)  # type: ignore

    @field_validator("text")
    @classmethod
    def validate_text(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("message cannot be empty or spaces only")
        return value


class MessageResponse(BaseModel):
    id: int
    chat_id: int
    text: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
