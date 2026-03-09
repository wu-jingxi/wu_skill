"use client";

import { useState } from "react";
import {
  ChatContainer,
  ChatMessage,
  ChatInput,
  TypingIndicator,
} from "../registry/blocks/chat";

type Message = {
  role: "user" | "assistant";
  content: string;
};

export function Chat() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [isLoading, setIsLoading] = useState(false);

  const handleSend = async (content: string) => {

    // 用户消息
    setMessages((prev) => [
      ...prev,
      { role: "user", content }
    ]);

    setIsLoading(true);

    try {

      const res = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          message: content
        })
      });

      const data = await res.json();

      // AI回复
      setMessages((prev) => [
        ...prev,
        { role: "assistant", content: data.reply }
      ]);

    } catch (err) {
      console.error(err);

      setMessages((prev) => [
        ...prev,
        { role: "assistant", content: "Server error" }
      ]);
    }

    setIsLoading(false);
  };

  return (
    <ChatContainer>

      {messages.map((msg, i) => (
        <ChatMessage
          key={i}
          role={msg.role}
          content={msg.content}
        />
      ))}

      {isLoading && <TypingIndicator />}

      <ChatInput
        onSubmit={handleSend}
        disabled={isLoading}
        placeholder="Type a message..."
      />

    </ChatContainer>
  );
}