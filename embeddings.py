from google import genai    # importing genai from google for generating embeddings
from dotenv import load_dotenv  # importing dotenv for loading API key from .env file
from sentence_transformers import SentenceTransformer  # for generating embeddings locally

from configuration import embedding_generator

import os 

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))  # calling api key for creating embeddings

# Create embedding from string, returns embedding
"""def get_embedding(text: str):
    response = client.models.embed_content(
        model="gemini-embedding-2", 
        contents=text
    )
    return response.embeddings[0].values"""
    
# Create embedding from string using local model with sentence transformer, returns embedding
def get_embedding(text: str):
    """model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )
    
    response = model.encode(
        text
    )"""
    
    response = embedding_generator.generate_embedding(text)
    
    return response

# Create embeddings from documents, return [] embeddings
def get_embeddings(document):
    embeddings=[]
    for doc in document:
        embedding = get_embedding(doc)
        embeddings.append(embedding)
    return embeddings
    