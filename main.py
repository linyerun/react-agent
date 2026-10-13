from tools import build_default_tools
import os
from llm import create_llm
from agent.loop import react_loop
from dotenv import load_dotenv

load_dotenv()

def main():
    # 获取模型配置
    api_key = os.environ.get("API_KEY")
    base_url = os.environ.get("BASE_URL")
    model = os.environ.get("MODEL")
    if not api_key:
        raise ValueError("未找到 API_KEY，请在 .env 文件中配置。")
    if not base_url:
        raise ValueError("未找到 BASE_URL，请在 .env 文件中配置。")
    if not model:
        raise ValueError("未找到 MODEL，请在 .env 文件中配置。")

    # 创建一个llm调用函数
    llm = create_llm(api_key, base_url, model)

    # 获取提供给llm调用的工具信息
    tools = build_default_tools()

    question = "请帮我计算 21+21，并统计答案字符串有多少个字符, 并且打印当前时间。"

    print("=" * 60)
    print("ReAct Agent 示例")
    print("可用工具：calculator / get_current_time / word_count")
    print("=" * 60)
    print("\n")
    print("*" * 60)
    print(f"User>\t {question}")
    print("*" * 60)

    # 执行ReAct Loop
    result = react_loop(question, tools, llm)

    print("\n")
    print("=" * 60)
    print(f"Assistant>\t {result}")
    print("=" * 60)


if __name__ == '__main__':
    main()
