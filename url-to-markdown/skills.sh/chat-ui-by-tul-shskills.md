---
url: https://skills.sh/tul-sh/skills/chat-ui
title: "chat-ui by tul-sh/skills"
description: "Discover and install skills for AI agents."
coverImage: "https://skills.sh/tul-sh/skills/chat-ui/opengraph-image?af71664f4dc3e62d"
captured_at: "2026-03-09T17:53:25.364Z"
---

# chat-ui by tul-sh/skills

[skills](https://skills.sh/) / [tul-sh](https://skills.sh/tul-sh) / [skills](https://skills.sh/tul-sh/skills) /chat-ui

## chat-ui

## Chat UI Components

Chat building blocks from [ui.inference.sh](https://ui.inference.sh/).

![Chat UI Components](https://skills.sh/api/image-proxy?url=https%3A%2F%2Fcloud.inference.sh%2Fapp%2Ffiles%2Fu%2F4mg21r6ta37mpaz6ktzwtt8krr%2F01kgvftp7hb8wby7z66fvs9asd.jpeg&s=fecead2d493b60f6)

## Quick Start

```bash
# Install chat components

npx shadcn@latest add https://ui.inference.sh/r/chat.json
```

## Components

### Chat Container

```tsx
import { ChatContainer } from "@/registry/blocks/chat/chat-container"

<ChatContainer>

  {/* messages go here */}

</ChatContainer>
```

### Messages

```tsx
import { ChatMessage } from "@/registry/blocks/chat/chat-message"

<ChatMessage

  role="user"

  content="Hello, how can you help me?"

/>

<ChatMessage

  role="assistant"

  content="I can help you with many things!"

/>
```

### Chat Input

```tsx
import { ChatInput } from "@/registry/blocks/chat/chat-input"

<ChatInput

  onSubmit={(message) => handleSend(message)}

  placeholder="Type a message..."

  disabled={isLoading}

/>
```

### Typing Indicator

```tsx
import { TypingIndicator } from "@/registry/blocks/chat/typing-indicator"

{isTyping && <TypingIndicator />}
```

## Full Example

```tsx
import {

  ChatContainer,

  ChatMessage,

  ChatInput,

  TypingIndicator,

} from "@/registry/blocks/chat"

export function Chat() {

  const [messages, setMessages] = useState([])

  const [isLoading, setIsLoading] = useState(false)

  const handleSend = async (content: string) => {

    setMessages(prev => [...prev, { role: 'user', content }])

    setIsLoading(true)

    // Send to API...

    setIsLoading(false)

  }

  return (

    <ChatContainer>

      {messages.map((msg, i) => (

        <ChatMessage key={i} role={msg.role} content={msg.content} />

      ))}

      {isLoading && <TypingIndicator />}

      <ChatInput onSubmit={handleSend} disabled={isLoading} />

    </ChatContainer>

  )

}
```

## Message Variants

| Role | Description |
| --- | --- |
| `user` | User messages (right-aligned) |
| `assistant` | AI responses (left-aligned) |
| `system` | System messages (centered) |

## Styling

Components use Tailwind CSS and shadcn/ui design tokens:

```tsx
<ChatMessage

  role="assistant"

  content="Hello!"

  className="bg-muted"

/>
```

## Related Skills

```bash
# Full agent component (recommended)

npx skills add inference-sh/skills@agent-ui

# Declarative widgets

npx skills add inference-sh/skills@widgets-ui

# Markdown rendering

npx skills add inference-sh/skills@markdown-ui
```

## Documentation

- [Chatting with Agents](https://inference.sh/docs/agents/chatting) - Building chat interfaces
- [Agent UX Patterns](https://inference.sh/blog/ux/agent-ux-patterns) - Chat UX best practices
- [Real-Time Streaming](https://inference.sh/blog/observability/streaming) - Streaming responses

Component docs: [ui.inference.sh/blocks/chat](https://ui.inference.sh/blocks/chat)

Weekly Installs

14

Repository

[tul-sh/skills](https://github.com/tul-sh/skills "tul-sh/skills")

GitHub Stars

126

First Seen

Feb 1, 2026

Installed on

claude-code9

opencode9

gemini-cli8

antigravity8

openclaw8

cursor8