# imports tools required for document reading from tools.py
from tools import (
    load_json, 
    load_pdf, 
    load_txt
)

import os

# Extract chunks & metadata from knowledge base
def get_chunks_metadatas():
    files = []
    chunks = []
    metadatas = []
    path = os.listdir("knowledge_base")
    for file in path:
        files.append(file)
    
    for file in files:
        file_path = f"knowledge_base/{file}"
        
        extention = os.path.splitext(file_path)[1]
        
        if extention == ".txt":
            chunks.append(load_txt(file_path))
            metadatas.append({
                "source": file
            })
        elif extention == ".pdf": 
            chunks.append(load_pdf(file_path))
            metadatas.append({
                "source": file
            })
        elif extention == ".json":
            chunks.append(load_json(file_path))
            metadatas.append({
                "source": file
            })
        else:
            raise ValueError("Unsupported file format")
    
    return chunks, metadatas