from state import state
from memory import memory

from tools import (
    recall_user, 
    find_missing_skills, 
    retrieve_documents, 
    placement_support
)

def create_state():
    return {
        "Memory": {},
        "Goal": "",
        "Skills": [],
        "MissingSkills": [],
        "RetrievedDocs": [],
        "LearningPlan": "",
        "UserQuestion": ""
    }

def run_agent(question):
    
    state = create_state()
    
    state["memory"] = memory

    state["UserQuestion"] = question

    state = recall_user(state)

    state = find_missing_skills(state)

    state = retrieve_documents(state)

    answer = placement_support(state)

    return answer
