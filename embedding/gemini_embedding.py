from embedding.base import BaseEmbedding

from google import genai
from dotenv import load_dotenv

import os

load_dotenv()

class GeminiEmbedding(BaseEmbedding):
    def __init__(self):
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    
    def generate_embedding(self, text):
        result = self.client.models.embed_content(
            model="gemini-embedding-2",
            contents=text
        )
        
        return result.embeddings[0].values