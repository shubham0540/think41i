import React, { useContext, useEffect } from "react";
import MessageList from "./MessageList";
import UserInput from "./UserInput";
import { ChatContext } from "../context/ChatContext";

export default function ChatWindow() {
  const { messages, sendMessage, fetchConversations, conversations, loadConversation } = useContext(ChatContext);

  useEffect(() => {
    fetchConversations();
  }, []);

  return (
    <div className="flex w-full h-screen">
      {/* Sidebar */}
      <div className="w-1/4 bg-gray-200 p-4 border-r">
        <h2 className="text-lg font-bold mb-3">Past Conversations</h2>
        {conversations.map((conv) => (
          <div
            key={conv.id}
            className="p-2 bg-white rounded-lg mb-2 cursor-pointer hover:bg-gray-300"
            onClick={() => loadConversation(conv.id)}
          >
            Conversation #{conv.id}
          </div>
        ))}
      </div>

      {/* Chat Window */}
      <div className="flex flex-col w-3/4 p-4">
        <MessageList messages={messages} />
        <UserInput onSend={sendMessage} />
      </div>
    </div>
  );
}
