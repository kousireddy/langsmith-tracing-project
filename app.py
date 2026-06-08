from dotenv import load_dotenv
from groq import Groq
from langsmith import traceable

load_dotenv()

# Groq Client
client = Groq()


@traceable(run_type="tool")
def get_context(question: str) -> str:
    """
    Simulated tool call.
    """
    return """
    LangSmith traces are stored for 14 days
    on the Developer plan.
    """


@traceable(run_type="llm")
def call_groq(messages):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0.7
    )

    return response.choices[0].message.content


@traceable
def assistant(question: str) -> str:

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