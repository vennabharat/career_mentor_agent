from memory import memory   # importing memory from memory.py

# state for managing tool output
state = {
    "memory": {},
    "goal": "",
    "skills": [],
    "missing_skills": [],
    "retrieved_docs": [],
    "learning_plan": "",
    "user_question": ""
}