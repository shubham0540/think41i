from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..schemas import ChatRequest, ChatResponse
from .. import crud, chat_service

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ Main Chat API
@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(req: ChatRequest, db: Session = Depends(get_db)):
    return chat_service.process_chat(req, db)

# ✅ Get all conversations for a user
@router.get("/conversations")
def list_conversations(user_id: int, db: Session = Depends(get_db)):
    conversations = crud.get_all_conversations(db, user_id)
    return [{"id": c.id, "created_at": c.created_at} for c in conversations]

# ✅ Get messages of a conversation
@router.get("/conversations/{conversation_id}")
def get_conversation(conversation_id: int, db: Session = Depends(get_db)):
    messages = crud.get_messages_for_conversation(db, conversation_id)
    return [{"sender": m.sender, "text": m.message} for m in messages]
