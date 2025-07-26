import React, { createContext, useState } from "react";
import { sendChatMessage, getConversations, getConversationHistory } from "../api/chatApi";

export const ChatContext = createContext();

export const ChatProvider = ({ children }) => {
  const [messages, setMessages] = useState([]);
  const [conversationId, setConversationId] = useState(null);
  const [conversations, setConversations] = useState([]);

  const sendMessage = async (text) => {
    setMessages((prev) => [...prev, { sender: "user", text }]);
    const res = await sendChatMessage(text, conversationId);
    setConversationId(res.conversation_id);
    setMessages((prev) => [...prev, { sender: "ai", text: res.response }]);
  };

  const fetchConversations = async () => {
    const res = await getConversations();
    setConversations(res);
  };

  const loadConversation = async (id) => {
    const history = await getConversationHistory(id);
    setConversationId(id);
    setMessages(history);
  };

  return (
    <ChatContext.Provider value={{ messages, sendMessage, conversations, fetchConversations, loadConversation }}>
      {children}
    </ChatContext.Provider>
  );
};
