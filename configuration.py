#configuration for LLM provider

from llm.factory import get_llm
from embedding.factory import get_embedding

llm = get_llm("gemini") # using gemini as LLM

# using sentence-transformer for embeddings
embedding_generator = get_embedding("sentence-transformers")   