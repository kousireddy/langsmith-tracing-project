from utils.config import *
from langsmith import traceable

from tools.context_tool import get_context
from llm.groq_client import call_groq


@traceable
def assistant(question: str):

    context = get_context(question)

    messages = [
        {
            "role": "system",
            "content": f"""
Use the provided context.

Context:
{context}
"""
        },
        {
            "role": "user",
            "content": question
        }
    ]

    return call_groq(messages)


if __name__ == "__main__":

    while True:

        question = input("\nYou: ")

        if question.lower() == "exit":
            break

        answer = assistant(question)

        print("\nAssistant:", answer)