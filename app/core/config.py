from pydantic import BaseModel

class Settings(BaseModel):
    database_url: str = "postgresql+psycopg2://postgres:postgres@db:5432/chats"

settings = Settings()
