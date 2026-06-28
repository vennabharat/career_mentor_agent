from google import genai    # importing genai from google for generating embeddings
from dotenv import load_dotenv  # importing dotenv for loading API key from .env file

import os 

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))  # calling api key for creating embeddings

# Create embedding from string, returns embedding
def get_embedding(text: str):
    embedding = client.models.embed_content(
        model="gemini-embedding-2", 
        contents=text
    )
    return embedding

# Create embeddings from documents, return [] embeddings
def get_embeddings(document):
    embeddings=[]
    for doc in document:
        embedding = get_embedding(doc)
        embeddings.append(embedding)
    return embeddings
    