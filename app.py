from graph.workflow import build_graph
from langchain_core.messages import HumanMessage

graph = build_graph()

thread_id = input(
    "Session ID: "
).strip() or "student_001"

config = {
    "configurable" : {
        "thread_id": thread_id
    }
}

while True:

    query = input("\nYou: ")
    
    if query.lower() == "exit":
        break

    result = graph.invoke(
        {
            "messages": [
                HumanMessage(content=query)
            ]
        },
        config=config
    )

    print(
        "\nAssistant:",
        result["messages"][-1].content
    )