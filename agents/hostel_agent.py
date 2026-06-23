from utils.llm import llm
from langchain_core.messages import AIMessage
from knowledge_base.hostel_kb import HOSTEL_KB

def hostel_agent(state):
    question = state["messages"][-1].content
    
    context= "\n".join(HOSTEL_KB.values())

    prompt = f"""
    You are a university hostel officer.
    Use ONLY the information below:

    Information: {context}

    Question: {question}

    Answer clearly and accurately.
    """

    result = llm.invoke(prompt)

    return {
        **state,
        "messages": [
            AIMessage(content=result.content)
        ]
    }
    