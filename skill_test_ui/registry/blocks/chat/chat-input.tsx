import { useState } from "react";

export function ChatInput({ 
  onSubmit, 
  disabled, 
  placeholder = "Type a message..." 
}: { 
  onSubmit: (msg: string) => void; 
  disabled: boolean;
  placeholder?: string;
}) {
  const [value, setValue] = useState("");

  const handleSend = () => {
    if (!value.trim()) return;
    onSubmit(value);
    setValue("");
  };

  return (
    <div className="mt-2 flex">
      <input
        className="border p-2 flex-1 rounded-l"
        value={value}
        onChange={(e) => setValue(e.target.value)}
        disabled={disabled}
        placeholder={placeholder}
      />
      <button className="bg-blue-500 text-white p-2 rounded-r" onClick={handleSend} disabled={disabled}>
        Send
      </button>
    </div>
  );
}