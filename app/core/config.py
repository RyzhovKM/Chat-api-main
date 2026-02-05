import os

from pydantic import BaseModel


class Settings(BaseModel):
    database_url: str = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg2://postgres:postgres@db:5432/chats",
    )


settings = Settings()
