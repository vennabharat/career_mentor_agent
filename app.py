from fastapi import FastAPI

from tools import(
    remember_user, 
    recall_user
)
from rag import (
    collection, 
    load_vector_database, 
    get_chunks_metadatas
)

app = FastAPI()

if collection.count() == 0:
    load_vector_database()
    
