import datetime
from . import crud
import requests
import os

def process_chat(req, db):
    conversation_id = req.conversation_id or crud.create_conversation(db, req.user_id)

    crud.save_message(db, conversation_id, "user", req.message)

    ai_response = f"Hello! You said: {req.message}"

    crud.save_message(db, conversation_id, "ai", ai_response)

    return {"conversation_id": conversation_id, "response": ai_response}



def get_llm_response(user_message: str):
    headers = {"Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}"}
    payload = {"prompt": user_message, "max_tokens": 100}
    r = requests.post("https://api.groq.com/v1/completions", json=payload, headers=headers)
    return r.json().get("choices", [{}])[0].get("text", "Sorry, I couldn't generate a response.")

def process_chat(req, db):
    conversation_id = req.conversation_id or create_conversation(db, req.user_id)

    save_message(db, conversation_id, "user", req.message)

    ai_response = get_llm_response(req.message)

    save_message(db, conversation_id, "ai", ai_response)

    return {"conversation_id": conversation_id, "response": ai_response}

