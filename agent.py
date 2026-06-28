from state import state     # importing state 
from memory import memory   # importing memory

from tools import (
    recall_user, 
    find_missing_skills, 
    retrieve_documents, 
    placement_support
)

def create_state():
    return {
        "memory": {},
        "goal": "",
        "skills": [],
        "missing_skills": [],
        "retrieved_docs": [],
        "learning_plan": "",
        "user_question": ""
    }

def run_agent(question):
    
    state = create_state()
    
    state["memory"] = memory

    state["user_question"] = question

    state = recall_user(state)

    state = find_missing_skills(state)

    state = retrieve_documents(state)

    answer = placement_support(state)

    return answer
