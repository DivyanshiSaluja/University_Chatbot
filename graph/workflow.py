from langgraph.graph import END, StateGraph
from graph.University_state import UniversityState
from graph.router import agent_router
from nodes.extractor_profile import extractor_profile
from nodes.classifier import classify_query

from agents.academic_agent import academic_agent
from agents.admission_agent import admission_agent
from agents.hostel_agent import hostel_agent
from agents.placement_agent import placement_agent
from  agents.memory_agent import memory_agent

from memory.checkpoint import memory

def build_graph():

    builder = StateGraph(UniversityState)

    builder.add_node(extractor_profile, name="extractor_profile")
    builder.add_node(classify_query, name="classify_query")
    builder.add_node(academic_agent, name="academic_agent")
    builder.add_node(admission_agent, name="admission_agent")
    builder.add_node(hostel_agent, name="hostel_agent")
    builder.add_node(placement_agent, name="placement_agent")
    builder.add_node(memory_agent, name="memory_agent")

    builder.set_entry_point("extractor_profile")
    builder.add_edge("extractor_profile", "classify_query")
    builder.add_conditional_edges(
        "classify_query",
        agent_router,
        {
            "admission": "admission_agent",
            "hostel": "hostel_agent",
            "placement": "placement_agent",
            "academic": "academic_agent",
            "memory": "memory_agent"
        }
    )

    builder.add_edge("academic_agent", END)
    builder.add_edge("admission_agent", END)
    builder.add_edge("hostel_agent", END)
    builder.add_edge("placement_agent", END)
    builder.add_edge("memory_agent", END)

    return builder.compile(
        checkpointer=memory
    )