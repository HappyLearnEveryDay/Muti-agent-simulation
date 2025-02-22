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
        self.messages = []
        self.client = None  # Initialize client as None
        
    def _ensure_client(self):
        """Ensure OpenAI client is initialized in current process"""
        if self.client is None:
            self.client = openai.OpenAI(
                api_key=self.api_key,
                base_url=self.base_url
            )
        
    def generate_response(self, conversation_history: List[Dict]) -> str:
        """Generate a response based on conversation history"""
        try:
            self._ensure_client()  # Initialize client if needed
            self.messages = [
                {"role": "system", "content": self.system_prompt}
            ] + conversation_history
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages,
                temperature=self.temperature
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            print(f"Agent Error in {self.name}: {str(e)}")
            return f"抱歉，我遇到了一些问题：{str(e)}"
