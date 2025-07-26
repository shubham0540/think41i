const BASE_URL = process.env.REACT_APP_API_URL || "http://localhost:8000/api";


export const sendChatMessage = async (message, conversation_id) => {
  const res = await fetch(`${BASE_URL}/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ user_id: 1, message, conversation_id }),
  });
  return res.json();
};

export const getConversations = async () => {
  const res = await fetch(`${BASE_URL}/conversations?user_id=1`);
  return res.json();
};

export const getConversationHistory = async (id) => {
  const res = await fetch(`${BASE_URL}/conversations/${id}`);
  return res.json();
};
