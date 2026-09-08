from fastapi import FastAPI

app = FastAPI(title="Multiagent IA")


def route_task(task_type: str) -> str:
    if task_type == "research":
        return "research_agent"
    elif task_type == "code":
        return "code_agent"
    else:
        return "general_agent"


@app.get("/")
def health_check():
    return {"status": "ok"}


@app.get("/route/{task_type}")
def route(task_type: str):
    agent = route_task(task_type)
    return {"task_type": task_type, "assigned_agent": agent}