def weather_tool():
    return {"weather": "广州今天25度晴天"}

def math_tool(number: int):
    return {"result": number * 2}
import subprocess
import json
import os
import platform
import time

def url_to_markdown_tool(url: str):
    """抓取网页并转换为 Markdown"""
    try:
        # 定义 Bun 脚本的完整路径
        script_path = ".agents/skills/baoyu-url-to-markdown/scripts/main.ts"
        
        # 执行命令 (注意：这里使用 bun run，确保你在该目录下能跑通)
        # 我们使用 cwd 参数指定工作目录，这样它就能找到自己的 node_modules
        result = subprocess.run(
            ["bun", "run", script_path, url],
            cwd=".",  # 根目录
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        
        if result.returncode == 0:
            return f"成功抓取！输出信息: {result.stdout.strip()}"
        else:
            return f"抓取失败: {result.stderr.strip()}"
            
    except Exception as e:
        return f"工具执行出错: {str(e)}"
    
import subprocess
import os
import webbrowser # 新增：用于自动弹窗
import time

def start_ui_tool():
    """启动前端和后端服务并自动打开浏览器"""
    base_dir = os.getcwd()
    ui_dir = os.path.join(base_dir, "skill_test_ui")
    
    try:
        # 1. 启动后端
        subprocess.Popen([".venv/Scripts/python.exe", "server.py"], cwd=base_dir)
        
        # 2. 启动前端
        subprocess.Popen(["npm", "run", "dev"], cwd=ui_dir, shell=True)
        
        # 3. 等待几秒，确保服务跑起来后再弹窗
        time.sleep(3) 
        webbrowser.open("http://localhost:3000")
        
        return "✅ 后端服务已启动，前端界面已在浏览器打开。"
    except Exception as e:
        return f"❌ 启动失败: {str(e)}"