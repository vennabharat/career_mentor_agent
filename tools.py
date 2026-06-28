from memory import memory   # importing memory from memory.py
from state import state     # importing state from state.py
from pypdf import PdfReader # importing pdf reader for extracting text from pdf files
from google import genai    # importing genai from google for callin LLM
from dotenv import load_dotenv  # importing dotenv for loading API key

import os
import json

load_dotenv()

# tool for saving user details
def remember_user():
    """For saving student details - name, goal & skills to the memory

    Returns:
        None
    """
    memory = {
        "Name": "Bharat", 
        "Goal": "AI Engineer", 
        "Skills": ["SQL", "Python"]
    }
    return "user saved to memory"

# tool for fetching user details to state
def recall_user():
    """fetches data from memory and update state 

    Returns:
        dict: updated state
    """
     
    state["Memory"] = memory
    state["Goal"] = memory.get("Goal")
    state["Skills"] = memory.get("Skills", [])
    
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
    
def tool_selection():
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
    
# for reading txt file
def load_txt(file_path):
    with open(file_path) as file:
        data = file.read()
    
    return data

# for reading pdf file
def load_pdf(file_path):
    reader = PdfReader(file_path)
    
    text = ""
    
    for page in reader.pages:
        text += page.extract_text() + "\n"
        
    return text

# for reading json file
def load_json(file_path):
    with open(file_path) as file:
        data = json.load(file)
        
    return json.dumps(data, indent=2)