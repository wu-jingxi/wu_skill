import json
import os
from openai import OpenAI
from my_tools import weather_tool, math_tool,url_to_markdown_tool,start_ui_tool

client = OpenAI(
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
    },
    {
        "type": "function",
        "function": {
            "name": "url_to_markdown_tool",
            "description": "当用户提供一个网页链接时，使用此工具将网页内容抓取并转换为 Markdown",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {"type": "string", "description": "网页的完整 URL"}
                },
                "required": ["url"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "start_ui_tool",
            "description": "启动前端和后端网页可视化界面。当用户想在浏览器中使用图形化聊天界面时使用。",
            "parameters": {
                "type": "object",
                "properties": {} # 不需要参数
            }
        }
    }

]


def run_agent(user_input):

    response = client.chat.completions.create(
        model="glm-4-flash",
        messages=[{"role": "user", "content": user_input}],
        tools=tools,
        tool_choice="auto"
    )

    message = response.choices[0].message

    # 如果模型想调用工具
    if message.tool_calls:

        tool_call = message.tool_calls[0]
        name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)

        '''print(f"\n⚠️ 模型想调用工具: {name}")
        print(f"参数: {args}")

        confirm = input("是否允许执行该工具？(yes/no): ")

        if confirm.lower() != "yes":
            return "❌ 工具调用被用户拒绝"'''

        # 执行工具
        if name == "weather_tool":
            result = weather_tool()

        elif name == "math_tool":
            result = math_tool(**args)
        elif name == "url_to_markdown_tool": # 新增这行
            result = url_to_markdown_tool(**args)
        elif name == "start_ui_tool":  # 新增
            result = start_ui_tool()
        else:
            return "未知工具"

        print(f"\n🔧 工具执行结果: {result}")

        # 把结果喂回模型
        second_response = client.chat.completions.create(
            model="glm-4-flash",
            messages=[
                {"role": "user", "content": user_input},
                message,
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result)
                }
            ]
        )

        final_answer = second_response.choices[0].message.content
        return final_answer

    # 如果没有工具调用
    else:
        return message.content


# CLI模式仍然可以用
def chat_loop():

    print("🤖 AI 已启动，输入 exit 退出")

    while True:

        user_input = input("\n你: ")

        if user_input == "exit":
            break

        reply = run_agent(user_input)

        print("\n🤖", reply)


if __name__ == "__main__":
    chat_loop()