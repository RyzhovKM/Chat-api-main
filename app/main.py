from fastapi import FastAPI
from app.api.routers.chats import router

app = FastAPI(title="Chat API")
app.include_router(router)
