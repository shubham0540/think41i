from . import crud
import os, requests

def get_llm_response(user_message: str):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return f"(Mock) AI Response to: {user_message}"

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "model": "mixtral-8x7b-32768",
        "messages": [{"role": "user", "content": user_message}],
    }
    try:
        res = requests.post(url, headers=headers, json=payload, timeout=10)
        res.raise_for_status()
        return res.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"(Error getting AI response) {e}"

def process_chat(req, db):
    conversation_id = req.conversation_id or crud.create_conversation(db, req.user_id)

    crud.save_message(db, conversation_id, "user", req.message)

    ai_response = get_llm_response(req.message)

    crud.save_message(db, conversation_id, "ai", ai_response)

    return {"conversation_id": conversation_id, "response": ai_response}
