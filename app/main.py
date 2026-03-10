from app.graph.chatbot_graph import app

def run_chatbot():
    print("AI Chatbot Started 🚀")

    while True:
        question = input("\nYou: ")

        result = app.invoke({
            "question": question
        })

        print("AI:", result["answer"])

if __name__ == "__main__":
    run_chatbot()