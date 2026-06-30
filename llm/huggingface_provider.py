from llm.base import BaseLLM

from transformers import pipeline

class huggingfaceLLM(BaseLLM):
    def __init__(self):
        self.model = pipeline(
            "text-generation",
            model="distilgpt2"
        )
    
    def generate(self, prompt):
        response = self.model(
            prompt,
            max_new_tokens = 50
        )
        return response[0]["generated_text"]