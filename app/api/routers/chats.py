from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.schemas.chat import ChatCreate, ChatResponse
from app.schemas.message import MessageCreate, MessageResponse
from app.services import chats as service
from app.core.logging import get_logger
from app.core.dependencies import get_db

router = APIRouter(prefix="/chats", tags=["Chats"])
logger = get_logger(__name__)


 

@router.post("/", response_model=ChatResponse, status_code=201)
def create_chat(data: ChatCreate, db: Session = Depends(get_db)):
    logger.info("Create chat request", extra={"title": data.title})

    chat = service.create_chat(db, data.title)

    logger.info(
        "Chat created",
        extra={"chat_id": chat.id, "title": chat.title},
    )
    return chat


@router.post("/{chat_id}/messages/", response_model=MessageResponse, status_code=201)
def create_message(chat_id: int, data: MessageCreate, db: Session = Depends(get_db)):
    logger.info(
        "Create message request",
        extra={"chat_id": chat_id, "text_length": len(data.text)},
    )

    message = service.create_message(db, chat_id, data.text)

    logger.info(
        "Message created",
        extra={"message_id": message.id, "chat_id": chat_id},
    )
    return message


@router.get("/{chat_id}")
def get_chat(
    chat_id: int,
    limit: int = Query(20, le=100),
    db: Session = Depends(get_db),
):
    logger.info(
        "Get chat request",
        extra={"chat_id": chat_id, "limit": limit},
    )

    chat, messages = service.get_chat_with_messages(db, chat_id, limit)

    logger.info(
        "Chat fetched",
        extra={
            "chat_id": chat_id,
            "messages_count": len(messages),
        },
    )

    return {
        "chat": ChatResponse.model_validate(chat),
        "messages": [MessageResponse.model_validate(m) for m in messages],
    }


@router.delete("/{chat_id}", status_code=204)
def delete_chat(chat_id: int, db: Session = Depends(get_db)):
    logger.info("Delete chat request", extra={"chat_id": chat_id})

    service.delete_chat(db, chat_id)

    logger.info("Chat deleted", extra={"chat_id": chat_id})
