from embedding.gemini_embedding import GeminiEmbedding
from embedding.sentence_transformer_embedding import Sentence_transformerEmbedding

def get_embedding(provider):
    
    if provider == "gemini":
        return GeminiEmbedding()
    
    if provider == "sentence-transformers":
        return Sentence_transformerEmbedding()
    
    raise ValueError("Unknow provider")