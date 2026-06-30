from embedding.base import BaseEmbedding

from sentence_transformers import SentenceTransformer

class Sentence_transformerEmbedding(BaseEmbedding):
    def __init__(self):
        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )
    
    def generate_embedding(self, text):
        result = self.model.encode(
            text
        )
        
        return result