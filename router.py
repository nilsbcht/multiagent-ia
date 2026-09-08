# agents/router.py
def route_task(task_type: str) -> str:
    if task_type == "research":
        return "research_agent"
    elif task_type == "code":
        return "code_agent"
    else:
        return "general_agent"