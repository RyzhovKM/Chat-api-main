from pydantic import BaseModel, constr, field_validator
from datetime import datetime

class ChatCreate(BaseModel):
    title: constr(min_length=1, max_length=200) # type: ignore

    @field_validator("title")
    @classmethod
    def validate_title(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("title cannot be empty or spaces only")
        return v
    
class ChatResponse(BaseModel):
    id: int
    title: str
    created_at: datetime

    class Config:
        from_attributes = True
