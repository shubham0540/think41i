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

def get_all_conversations(db: Session, user_id: int):
    return db.query(models.Conversation).filter(models.Conversation.user_id == user_id).all()

def get_messages_for_conversation(db: Session, conversation_id: int):
    return db.query(models.Message).filter(models.Message.conversation_id == conversation_id).order_by(models.Message.created_at).all()

