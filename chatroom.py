from typing import List, Dict
from agent import Agent
import time

class ChatRoom:
    def __init__(self, name: str, max_history_length: int = 50):
        self.name = name
        self.agents: List[Agent] = []
        self.conversation_history: List[Dict] = []
        self.max_history_length = max_history_length
        
    def add_agent(self, agent: Agent):
        self.agents.append(agent)
        
    def start_conversation(self, initial_prompt: str, num_rounds: int):
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
                
                # Truncate overall history if too long
                if len(self.conversation_history) > self.max_history_length:
                    summary = self._summarize_old_messages(self.conversation_history[:len(self.conversation_history)//2])
                    self.conversation_history = [{"role": "system", "content": summary}] + \
                                             self.conversation_history[len(self.conversation_history)//2:]
                
                print(f"{agent.name}: {response}")
                time.sleep(1)
    
    def _summarize_old_messages(self, messages: List[Dict]) -> str:
        """Create a summary of older messages"""
        summary = "之前的对话概要："
        for msg in messages[-5:]:  # Summarize last 5 messages from the old history
            if msg['role'] != 'system':
                name = msg.get('name', 'User')
                summary += f"{name}: {msg['content'][:30]}... "
        return summary
