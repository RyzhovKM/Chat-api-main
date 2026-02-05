from datetime import datetime
from sqlalchemy import ForeignKey, Text, DateTime, func, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True)
    chat_id: Mapped[int] = mapped_column(
        ForeignKey("chats.id", ondelete="CASCADE")
    )
    text: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    __table_args__ = ( 
        CheckConstraint(
            "length(trim(text)) > 0",
            name="check_message_text_not_empty",
        ),
    )

    chat: Mapped["Chat"] = relationship(back_populates="messages")
