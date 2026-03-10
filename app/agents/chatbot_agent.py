from app.services.llm_service import ask_llm

def chatbot_agent(state):
    question = state["question"]

    answer = ask_llm(question)

    return {
        "answer": answer
    }