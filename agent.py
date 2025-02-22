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
        self.memory_length = config.get("memory_length", 5)  # Default to remember last 5 messages
        
    def generate_response(self, conversation_history: List[Dict]) -> str:
        """Generate a response based on truncated conversation history"""
        # Only take recent messages based on memory_length
        recent_history = conversation_history[-self.memory_length:] if len(conversation_history) > self.memory_length else conversation_history
        
        # Add summary if there are earlier messages
        
        if len(conversation_history) > self.memory_length:
            summary = self._create_context_summary(conversation_history[:-self.memory_length])
            recent_history.insert(0, {"role": "system", "content": summary})
        
        self.messages = [
            {"role": "system", "content": self.system_prompt}
        ] + recent_history
        
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

    def _create_context_summary(self, older_messages: List[Dict]) -> str:
        """Create a brief summary of older messages"""
        return f"之前的对话要点：{' '.join([msg['content'][:50] + '...' for msg in older_messages[-2:]])}"
