from fastapi import FastAPI
from openai import OpenAI
import json
from my_tools import weather_tool, math_tool

app = FastAPI()

# ⚠️ 改成你的智谱 API Key
client = OpenAI(
    api_key="171a7d741b134da8b0884fa4dbd0a5ef.DDR6OONQhqWbnY7s",
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)

tools = [
    {
        "type": "function",
        "function": {
            "name": "weather_tool",
            "description": "查询天气",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },
    {
        "type": "function",
        "name": "math_tool",
        "function": {
            "name": "math_tool",
            "description": "计算一个数字的两倍",
            "parameters": {
                "type": "object",
                "properties": {
                    "number": {
                        "type": "integer"
                    }
                },
                "required": ["number"]
            }
        }
    }
]

@app.post("/chat")
def chat(user_input: str):

    response = client.chat.completions.create(
        model="glm-4-flash",
        messages=[{"role": "user", "content": user_input}],
        tools=tools,
        tool_choice="auto"
    )

    message = response.choices[0].message

    # 如果模型调用了工具
    if message.tool_calls:

        tool_call = message.tool_calls[0]
        name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)

        if name == "weather_tool":
            result = weather_tool()
        elif name == "math_tool":
            result = math_tool(**args)

        return {
            "tool_called": name,
            "tool_result": result
        }

    # 如果模型没调用工具
    return {"answer": message.content}