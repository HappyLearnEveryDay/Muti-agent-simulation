from agent import Agent
from chatroom import ChatRoom
from process_manager import ProcessManager
import textwrap

AGENTS = [
    {
        "name": "Alice",
        "system_prompt": textwrap.dedent("""
            你是Alice，具有以下特点：
            1. 善于提出问题
            2. 性格温和友善
            3. 喜欢帮助他人
        """),
        "model": "deepseek-chat",
        "api_key": "sk-787e14578cd44719b8ba8bdca63c45b6",
        "base_url": "https://api.deepseek.com/v1",
        "temperature": 0.7,
        "context_window": 3,
        "max_tokens": 250,     # 提高到 250
        "handle_truncation": True
    },
    {
        "name": "Bob",
        "system_prompt": textwrap.dedent("""
            你是Bob，具有以下特点：
            1. 逻辑思维清晰
            2. 直接坦率
            3. 善于分析问题
        """),
        "model": "deepseek-chat",
        "api_key": "sk-787e14578cd44719b8ba8bdca63c45b6",
        "base_url": "https://api.deepseek.com/v1",
        "temperature": 0.5,
        "context_window": 5,
        "max_tokens": 300,     # 提高到 300
        "handle_truncation": True
    },
    {
        "name": "Charlie",
        "system_prompt": textwrap.dedent("""
            你是Charlie，具有以下特点：
            1. 富有创造力
            2. 思维发散
            3. 善于提供新观点
        """),
        "model": "deepseek-chat",
        "api_key": "sk-787e14578cd44719b8ba8bdca63c45b6",
        "base_url": "https://api.deepseek.com/v1",
        "temperature": 0.8,
        "context_window": 2,
        "max_tokens": 200,     # 提高到 200
        "handle_truncation": True
    },
    {
        "name": "Diana",
        "system_prompt": textwrap.dedent("""
            你是Diana，具有以下特点：
            1. 擅长总结归纳
            2. 思维缜密严谨
            3. 善于提供建设性意见
        """),
        "model": "deepseek-chat",
        "api_key": "sk-787e14578cd44719b8ba8bdca63c45b6",
        "base_url": "https://api.deepseek.com/v1",
        "temperature": 0.6,
        "context_window": 4,
        "max_tokens": 300,     # 提高到 300
        "handle_truncation": True
    },
    {
        "name": "Eric",
        "system_prompt": textwrap.dedent("""
            你是Eric，具有以下特点：
            1. 幽默风趣
            2. 善于活跃气氛
            3. 经常用比喻来解释复杂概念
        """),
        "model": "deepseek-chat",
        "api_key": "sk-787e14578cd44719b8ba8bdca63c45b6",
        "base_url": "https://api.deepseek.com/v1",
        "temperature": 0.9,
        "context_window": 2,
        "max_tokens": 250,     # 提高到 250
        "handle_truncation": True
    },
    {
        "name": "Fiona",
        "system_prompt": textwrap.dedent("""
            你是Fiona，具有以下特点：
            1. 充满好奇心
            2. 喜欢探索新观点
            3. 经常从不同角度思考问题
        """),
        "model": "deepseek-chat",
        "api_key": "sk-787e14578cd44719b8ba8bdca63c45b6",
        "base_url": "https://api.deepseek.com/v1",
        "temperature": 0.75,
        "context_window": 3,
        "max_tokens": 250,     # 提高到 250
        "handle_truncation": True
    },
    {
        "name": "George",
        "system_prompt": textwrap.dedent("""
            你是George，具有以下特点：
            1. 理性客观
            2. 擅长数据分析
            3. 总是用事实支持观点
        """),
        "model": "deepseek-chat",
        "api_key": "sk-787e14578cd44719b8ba8bdca63c45b6",
        "base_url": "https://api.deepseek.com/v1",
        "temperature": 0.4,
        "context_window": 5,
        "max_tokens": 300,     # 提高到 300
        "handle_truncation": True
    },
    {
        "name": "Hannah",
        "system_prompt": textwrap.dedent("""
            你是Hannah，具有以下特点：
            1. 富有同理心
            2. 善于从人文角度思考
            3. 关注科技对人类情感和关系的影响
        """),
        "model": "deepseek-chat",
        "api_key": "sk-787e14578cd44719b8ba8bdca63c45b6",
        "base_url": "https://api.deepseek.com/v1",
        "temperature": 0.65,
        "context_window": 4,
        "max_tokens": 300,     # 提高到 300
        "handle_truncation": True
    },
    {
        "name": "Ian",
        "system_prompt": textwrap.dedent("""
            你是Ian，具有以下特点：
            1. 哲学思维
            2. 善于提出深层次问题
            3. 经常探讨事物的本质和伦理影响
        """),
        "model": "deepseek-chat",
        "api_key": "sk-787e14578cd44719b8ba8bdca63c45b6",
        "base_url": "https://api.deepseek.com/v1",
        "temperature": 0.85,
        "context_window": 6,
        "max_tokens": 350,     # 提高到 350
        "handle_truncation": True
    }
]

def main():
    # Create and start process manager
    process_manager = ProcessManager(AGENTS)
    process_manager.start_rooms()

if __name__ == "__main__":
    main()
