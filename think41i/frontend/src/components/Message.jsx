export default function Message({ sender, text }) {
  const isUser = sender === "user";
  return (
    <div
      className={`p-2 my-1 rounded-lg max-w-[70%] ${
        isUser ? "bg-blue-500 text-white ml-auto" : "bg-gray-200 text-black mr-auto"
      }`}
    >
      {text}
    </div>
  );
}
