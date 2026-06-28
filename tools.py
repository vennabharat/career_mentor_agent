from memory import memory   # importing memory from memory.py
from state import state     # importing state from state.py
from google import genai    # importing genai from google for callin LLM
from dotenv import load_dotenv  # importing dotenv for loading API key
from rag import get_relevant_chunks # for fetching relevant chunks using RAG

import os

load_dotenv()

# tool for saving user details
def remember_user():
    """For saving student details - name, goal & skills to the memory

    Returns:
        None
    """
    memory["Name"] = "Bharat"
    memory["Goal"] = "AI Engineer"
    memory["Skills"] = ["SQL", "Python"]
    return "user saved to memory"

# tool for fetching user details to state
def recall_user(state):
    """fetches data from memory and update state 

    Returns:
        dict: updated state
    """
     
    state["Memory"] = memory
    state["Goal"] = memory.get("Goal")
    state["Skills"] = memory.get("Skills", [])
    
    return state

def find_missing_skills(state):
    required_skills = [
        "Python",
        "FastAPI",
        "ChromaDB",
        "Memory",
        "RAG",
        "Docker"
    ]
    missing = []
    for skill in required_skills:
        if skill not in state["Skills"]:
            missing.append(skill)
    state["MissingSkills"] = missing
    
    return state

def retrieve_documents(state):
    chunks = get_relevant_chunks(state["UserQuestion"])

    state["RetrievedDocs"] = chunks
    
    return state

# RAG for retriving relevant chunks from knowledge_base to state
def placement_support(state):
    """LLM response by understanding user goal, skills, missing skills and suggests lesson plan

    Returns:
        str: response from LLM
    """
    context = state
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=f"""
        You're a placement mentor. You provide guidence 
        
        context: {context}
        """
    )
    
    return response.text
    
def tool_router():
    """LLM funtion calling

    Returns:
        None: LLM Chooses function to respond
    """
    tools = [
        remember_user,
        recall_user, 
        placement_support
    ]
    
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
        Choose from the following tools
        
        tools: {tools}
        """
    )
