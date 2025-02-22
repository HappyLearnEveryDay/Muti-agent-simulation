from agent import Agent
from chatroom import ChatRoom
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
        "memory_length": 4  # Remember last 4 messages
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
        "memory_length": 3  # Bob has shorter memory
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
        "memory_length": 5  # Charlie has longer memory
    }
]

def main():
    # Create chatroom
    chatroom = ChatRoom("Main Room")
    
    # Create and add agents
    for agent_config in AGENTS:
        agent = Agent(agent_config)
        chatroom.add_agent(agent)
    
    # Start conversation
    initial_prompt = "让我们讨论一下AI时代下,对话式编程工程师的前景 。"
    chatroom.start_conversation(initial_prompt, num_rounds=5)

if __name__ == "__main__":
    main()
