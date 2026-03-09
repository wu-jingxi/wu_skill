export function ChatMessage({ role, content }: { role: "user" | "assistant"; content: string }) {
  return (
    <div className={role === "user" ? "text-right" : "text-left"}>
      <p className="inline-block bg-gray-200 p-2 rounded">{content}</p>
    </div>
  );
}