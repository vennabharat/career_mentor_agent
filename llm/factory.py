from llm.gemini_provider import GeminiLLM
from llm.huggingface_provider import huggingfaceLLM


def get_llm(provider):
    
    if provider == "gemini":
        return GeminiLLM()
    
    if provider == "huggingface":
        return huggingfaceLLM()
    
    raise ValueError("Unknown provider")