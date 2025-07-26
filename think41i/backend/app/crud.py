from . import models
from sqlalchemy.orm import Session
import datetime

def create_conversation(db: Session, user_id: int):
    conv = models.Conversation(user_id=user_id, created_at=datetime.datetime.utcnow())
    db.add(conv)
    db.commit()
    db.refresh(conv)
    return conv.id

def save_message(db: Session, conversation_id: int, sender: str, text: str):
    msg = models.Message(
        conversation_id=conversation_id,
        sender=sender,
        message=text,
        created_at=datetime.datetime.utcnow()
    )
    db.add(msg)
    db.commit()
    return msg
