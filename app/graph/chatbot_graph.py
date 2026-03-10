from langgraph.graph import StateGraph, END
from app.schemas.state_schema import ChatState
from app.agents.chatbot_agent import chatbot_agent

graph = StateGraph(ChatState)

graph.add_node("chatbot", chatbot_agent)

graph.set_entry_point("chatbot")

graph.add_edge("chatbot", END)

app = graph.compile()