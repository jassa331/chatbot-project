from langchain_groq import ChatGroq
from app.config.settings import OPENAI_API_KEY, MODEL_NAME

llm = ChatGroq(
    api_key=OPENAI_API_KEY,
    model=MODEL_NAME
)

def ask_llm(question: str):
    response = llm.invoke(question)
    return response.content
