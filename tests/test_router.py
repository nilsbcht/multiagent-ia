# tests/test_router.py
from router import route_task


def test_route_research():
    assert route_task("research") == "research_agent"

def test_route_code():
    assert route_task("code") == "code_agent"

def test_route_unknown():
    assert route_task("blabla") == "general_agent"