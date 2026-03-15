import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def ai_clean(text: str) -> str:
    if not OPENAI_API_KEY:
        return "AI agent skipped: No OpenAI API key found."

    from langchain_openai import ChatOpenAI
    from langchain.schema import HumanMessage, SystemMessage

    llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=OPENAI_API_KEY)

    system_prompt = """You are a data cleaning expert.
    Given raw tabular data as text, identify and fix:
    - Missing values
    - Duplicates
    - Incorrect data types
    Return a cleaned version of the data."""

    MAX_CHARS = 2000
    chunks = [text[i:i+MAX_CHARS] for i in range(0, len(text), MAX_CHARS)]
    results = []

    for chunk in chunks:
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=f"Clean this data:\n{chunk}")
        ]
        response = llm.invoke(messages)
        results.append(response.content)

    return "\n".join(results)
