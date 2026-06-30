def prompt_builder(state):
    prompt = f"""
    goal = {state["goal"]}
    
    skilss = {state["skills"]}
    
    missing skills = {state["missing_skills"]}
    
    retrieved documents = {state["retrieved_docs"]}
    
    learning plan = {state["learning_plan"]}
    
    user question = {state["user_question"]}
    """
    return prompt