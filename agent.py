from typing import Dict, List
import openai

class Agent:
    def __init__(self, config: Dict):
        self.name = config["name"]
        self.system_prompt = config["system_prompt"]
        self.model = config["model"]
        self.api_key = config["api_key"]
        self.base_url = config["base_url"]
        self.temperature = config["temperature"]
        self.context_window = config.get("context_window", 3)  # Default to last 3 messages
        self.max_tokens = config.get("max_tokens", 250)  # 提高默认值到 250
        self.handle_truncation = config.get("handle_truncation", True)  # 新增截断处理标志
        self.messages = []
        self.client = None  # Initialize client as None
        
    def _ensure_client(self):
        """Ensure OpenAI client is initialized in current process"""
        if self.client is None:
            self.client = openai.OpenAI(
                api_key=self.api_key,
                base_url=self.base_url
            )
        
    def _trim_conversation_history(self, history: List[Dict]) -> List[Dict]:
        """Keep only the most recent messages based on context window"""
        if len(history) <= self.context_window:
            return history
        return history[-self.context_window:]

    def _handle_truncated_response(self, response: str) -> str:
        """处理可能被截断的回复"""
        if not self.handle_truncation:
            return response
            
        # 常见的句子结束符号
        end_marks = ['.', '。', '!', '！', '?', '？']
        
        # 如果最后一个字符不是句子结束符号，尝试在最后一个完整句子处截断
        if response and response[-1] not in end_marks:
            last_pos = -1
            for mark in end_marks:
                pos = response.rfind(mark)
                last_pos = max(last_pos, pos)
            
            if last_pos > 0:
                response = response[:last_pos + 1]
                response = response.strip()
            
            # 添加省略号表示被截断
            response += "..."
            
        return response

    def generate_response(self, conversation_history: List[Dict]) -> str:
        """Generate a response based on conversation history"""
        try:
            self._ensure_client()  # Initialize client if needed
            trimmed_history = self._trim_conversation_history(conversation_history)
            self.messages = [
                {"role": "system", "content": self.system_prompt}
            ] + trimmed_history
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages,
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )
            
            content = response.choices[0].message.content
            return self._handle_truncated_response(content)
            
        except Exception as e:
            print(f"Agent Error in {self.name}: {str(e)}")
            return f"抱歉，我遇到了一些问题：{str(e)}"
