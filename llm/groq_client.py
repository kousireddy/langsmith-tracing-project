from groq import Groq
from langsmith import traceable

client = Groq()


@traceable(run_type="llm")
def call_groq(messages):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0.7
    )

    return response.choices[0].message.content