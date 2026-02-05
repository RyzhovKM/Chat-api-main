from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.chat import Chat
from app.models.message import Message

def create_chat(db: Session, title: str):
    chat = Chat(title=title.strip())
    db.add(chat)
    db.commit()
    db.refresh(chat)
    return chat

def get_chat(db: Session, chat_id: int):
    chat = db.get(Chat, chat_id)
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")
    return chat

def create_message(db: Session, chat_id: int, text: str):
    chat = get_chat(db, chat_id)
    message = Message(chat_id=chat.id, text=text.strip())
    db.add(message)
    db.commit()
    db.refresh(message)
    return message

def get_chat_with_messages(db: Session, chat_id: int, limit: int):
    chat = get_chat(db, chat_id)
    messages = (
        db.query(Message)
        .filter(Message.chat_id == chat_id)
        .order_by(Message.created_at.desc())
        .limit(limit)
        .all()
    )
    return chat, list(reversed(messages))

def delete_chat(db: Session, chat_id: int):
    chat = get_chat(db, chat_id)
    db.delete(chat)
    db.commit()
