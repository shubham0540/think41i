import React from "react";
import Message from "./Message";

export default function MessageList({ messages }) {
  return (
    <div className="flex flex-col p-4 overflow-y-auto h-[70vh] bg-white rounded-xl shadow-inner">
      {messages.map((msg, idx) => (
        <Message key={idx} sender={msg.sender} text={msg.text} />
      ))}
    </div>
  );
}
