from langgraph.graph import StateGraph, START
from langgraph.prebuilt import ToolNode, tools_condition

from .state import RagState
from .llm import llm_model
from .tools import tools

llm_with_tools = llm_model.bind_tools(tools)


def chatbot(state: RagState):
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": [response]}


graph = StateGraph(RagState)

graph.add_node("chatbot", chatbot)
graph.add_node("tools", ToolNode(tools))

graph.add_edge(START, "chatbot")

graph.add_conditional_edges(
    "chatbot",
    tools_condition,
)

graph.add_edge("tools", "chatbot")

app = graph.compile()