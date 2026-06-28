from chromadb import chromadb
from documents_loader import get_chunks_metadatas
from embeddings import (
    get_embeddings, 
    get_embedding
)

import uuid

# creating vector database
client = chromadb.PersistentClient(
    path="./chromaDB"
) 

collection = client.create_collection(
    name = "knowledge"
)

# load vector database with knowledge_base
def load_vector_database():
    chunks, metadatas = get_chunks_metadatas()
    ids = [
        [str(uuid.uuid4())]
        for _ in chunks
        ]
    
    collection.add(
        documents=chunks, 
        embeddings=get_embeddings(chunks), 
        metadatas=metadatas, 
        ids=ids
    )
    return "vector database loaded"

# retrive relevant chunks
def get_relevant_chunks(query):
    query_embedding = get_embedding(query)
    result = collection.query(
        query_embeddings=query_embedding,
        n_results=3, 
        include=["documents", "metadatas"]
    )
    return result