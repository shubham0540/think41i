import React from "react";

export default function Message({ sender, text }) {
  return (
    <div className={`p-2 my-1 max-w-md rounded-xl ${sender === "user" ? "bg-blue-500 text-white ml-auto" : "bg-gray-300 text-black mr-auto"}`}>
      {text}
    </div>
  );
}
