import React, { useEffect, useContext } from "react";
import MessageList from "./MessageList";
import UserInput from "./UserInput";
import { ChatContext } from "../context/ChatContext";

export default function ChatWindow() {
  const { messages, sendMessage, conversations, fetchConversations, loadConversation } =
    useContext(ChatContext);

  useEffect(() => {
    fetchConversations(); // ✅ load past chats
  }, []);

  return (
    <div className="flex w-3/4 h-[90vh] bg-white shadow-lg rounded-lg">
      {/* ✅ Sidebar */}
      <div className="w-1/4 border-r p-4 overflow-y-auto">
        <h2 className="font-bold mb-2">Conversations</h2>
        {conversations.map((c) => (
          <div
            key={c.id}
            onClick={() => loadConversation(c.id)}
            className="cursor-pointer p-2 hover:bg-gray-200 rounded"
          >
            Chat #{c.id}
          </div>
        ))}
      </div>

      {/* ✅ Chat Section */}
      <div className="flex flex-col w-3/4">
        <MessageList messages={messages} />
        <UserInput onSend={sendMessage} />
      </div>
    </div>
  );
}
