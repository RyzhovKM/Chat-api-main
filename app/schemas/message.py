from pydantic import BaseModel, constr, field_validator
from datetime import datetime

class MessageCreate(BaseModel):
    text: constr(min_length=1, max_length=5000) # type: ignore

    @field_validator("text")
    @classmethod
    def validate_text(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("message cannot be empty or spaces only")
        return v

class MessageResponse(BaseModel):
    id: int
    chat_id: int
    text: str
    created_at: datetime

    class Config:
        from_attributes = True
