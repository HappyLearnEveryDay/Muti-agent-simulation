from typing import List, Dict
from agent import Agent
import time

class ChatRoom:
    def __init__(self, name: str):
        self.name = name
        self.agents: List[Agent] = []
        self.conversation_history: List[Dict] = []
        
    def add_agent(self, agent: Agent):
        self.agents.append(agent)
        
    def start_conversation(self, initial_prompt: str, num_rounds: int):
        """Start a conversation between agents for specified number of rounds"""
        # Add initial prompt to conversation
        self.conversation_history.append({
            "role": "user",
            "content": initial_prompt
        })
        
        for round in range(num_rounds):
            print(f"\nRound {round + 1}")
            print("-" * 50)
            
            for agent in self.agents:
                response = agent.generate_response(self.conversation_history)
                message = {
                    "role": "assistant",
                    "content": response,
                    "name": agent.name
                }
                self.conversation_history.append(message)
                
                print(f"{agent.name}: {response}")
                time.sleep(1)  # Add small delay between messages
