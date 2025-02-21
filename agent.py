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
        
    def generate_response(self, conversation_history: List[Dict]) -> str:
        """Generate a response based on conversation history"""
        self.messages = [
            {"role": "system", "content": self.system_prompt}
        ] + conversation_history
        
        client = openai.OpenAI(
            api_key=self.api_key,
            base_url=self.base_url
        )
        
        response = client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            temperature=self.temperature
        )
        
        return response.choices[0].message.content
