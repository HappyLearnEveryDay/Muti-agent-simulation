import multiprocessing
from typing import List, Dict
import os
import logging
import time
import traceback

class ProcessManager:
    def __init__(self, all_agents: List[Dict]):
        self.all_agents = all_agents
        self.processes = []
        multiprocessing.set_start_method('spawn', force=True)  # Force spawn method
        
    @staticmethod
    def _run_room(room_name: str, agent_configs: List[Dict], initial_prompt: str, num_rounds: int):
        """Run chatroom in a separate process"""
        try:
            # Import dependencies inside process
            import sys
            sys.path.append(os.path.dirname(os.path.dirname(__file__)))
            
            from chatroom import ChatRoom
            from agent import Agent
            
            # Initialize room and agents
            chatroom = ChatRoom(room_name)
            for config in agent_configs:
                agent = Agent(config)
                chatroom.add_agent(agent)
            
            chatroom.start_conversation(initial_prompt, num_rounds)
            
        except Exception as e:
            print(f"\n[{room_name}] Error: {str(e)}")
            print(traceback.format_exc())
    
    def start_rooms(self):
        """Start multiple chatroom processes"""
        print("\n=== 聊天室启动信息 ===")
        print(f"日志文件位置: {os.path.abspath('chat_logs')}")
        
        # Split agents into groups
        agent_groups = [
            self.all_agents[i:i+3] for i in range(0, len(self.all_agents), 3)
        ]
        
        print(f"正在启动 {len(agent_groups)} 个聊天室...")
        
        # Create and start processes
        for i, group in enumerate(agent_groups):
            room_name = f"Room-{i+1}"
            try:
                process = multiprocessing.Process(
                    target=self._run_room,
                    args=(room_name, group, f"欢迎来到{room_name}！让我们讨论一下人工智能对未来社会的影响。", 2),
                    name=room_name,
                    daemon=False
                )
                self.processes.append(process)
                process.start()
                print(f"[{room_name}] 进程已启动 (PID: {process.pid})")
                time.sleep(2)  # Increased delay between starts
                
            except Exception as e:
                print(f"[{room_name}] 启动失败: {str(e)}")
                print(traceback.format_exc())
        
        # Wait for processes
        for process in self.processes:
            try:
                process.join()
            except Exception as e:
                print(f"[{process.name}] 等待进程时出错: {str(e)}")
