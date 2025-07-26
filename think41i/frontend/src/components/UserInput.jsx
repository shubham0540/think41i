import React, { useState } from "react";

export default function UserInput({ onSend }) {
  const [input, setInput] = useState("");

  const handleSend = () => {
    if (input.trim()) {
      onSend(input);
      setInput("");
    }
  };

  return (
    <div className="flex gap-2 mt-2">
      <input
        className="flex-1 p-2 border rounded-xl"
        placeholder="Type a message..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && handleSend()}
      />
      <button className="bg-blue-600 text-white px-4 py-2 rounded-xl" onClick={handleSend}>
        Send
      </button>
    </div>
  );
}
