from typing import List, Dict
from agent import Agent
import time
from logger import RoomLogger
import logging
import traceback

class ChatRoom:
    def __init__(self, name: str):
        self.name = name
        self.agents: List[Agent] = []
        self.conversation_history: List[Dict] = []
        # 延迟logger初始化到start_conversation方法
        self.logger = None
        
    def add_agent(self, agent: Agent):
        self.agents.append(agent)
        
    def start_conversation(self, initial_prompt: str, num_rounds: int):
        try:
            self.logger = RoomLogger.setup_logger(self.name)
            self.logger.info(f"\n{self.name} 开始对话")
            self.logger.info(f"初始提示: {initial_prompt}")
            self.logger.info(f"参与对话的智能体: {[agent.name for agent in self.agents]}")
            
            self.conversation_history.append({
                "role": "user",
                "content": initial_prompt
            })
            
            for round in range(num_rounds):
                self.logger.info(f"\nRound {round + 1}")
                
                for agent in self.agents:
                    response = agent.generate_response(self.conversation_history)
                    message = {
                        "role": "assistant",
                        "content": response,
                        "name": agent.name
                    }
                    self.conversation_history.append(message)
                    
                    # Log each message with flush
                    log_msg = f"{agent.name}: {response}"
                    self.logger.info(log_msg)
                    
                    # Force flush after each message
                    for handler in self.logger.handlers:
                        handler.flush()
                    
                    time.sleep(1)
                    
        except Exception as e:
            print(f"ChatRoom Error in {self.name}: {str(e)}")
            print(traceback.format_exc())
            if self.logger:
                self.logger.error(f"Error in conversation: {str(e)}")
                self.logger.error(traceback.format_exc())
            raise
