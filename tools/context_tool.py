from langsmith import traceable


@traceable(run_type="tool")
def get_context(question: str):

    knowledge_base = {
        "python": "Python is a high-level programming language.",
        "langsmith": "LangSmith traces are stored for 14 days on the Developer plan."
    }

    question = question.lower()

    if "python" in question:
        return knowledge_base["python"]

    if "langsmith" in question:
        return knowledge_base["langsmith"]

    return "No information found."