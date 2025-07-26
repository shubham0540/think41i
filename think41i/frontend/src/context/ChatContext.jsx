import React, { createContext, useState } from "react";
import {
  sendChatMessage,
  getConversations,
  getConversationHistory,
} from "../api/chatApi";

export const ChatContext = createContext();

export const ChatProvider = ({ children }) => {
  const [messages, setMessages] = useState([]);
  const [conversationId, setConversationId] = useState(null);
  const [conversations, setConversations] = useState([]);

  const fetchConversations = async () => {
    const data = await getConversations();
    setConversations(data);
  };

  const loadConversation = async (id) => {
    setConversationId(id);
    const history = await getConversationHistory(id);
    setMessages(history);
  };

  const sendMessage = async (text) => {
    const res = await sendChatMessage(text, conversationId);
    setConversationId(res.conversation_id);
    setMessages((prev) => [...prev, { sender: "user", text }, { sender: "ai", text: res.response }]);
    fetchConversations(); // refresh sidebar
  };

  return (
    <ChatContext.Provider
      value={{
        messages,
        sendMessage,
        conversations,
        fetchConversations,
        loadConversation,
      }}
    >
      {children}
    </ChatContext.Provider>
  );
};
