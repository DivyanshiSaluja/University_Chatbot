from utils.llm import llm
from graph.University_state import UniversityState
import json

def extractor_profile(state):
    """
    Detects if the user mentioned their name, register number, or department.
    Updates state fields if found.
    """
    last_msg = state["messages"][-1].content
    
    # Simple rule based extraction first

    if "my name id" in last_msg:
        try:
            name=last_msg.split("my name is")[1].strip().split()[0]
            state["student_name"] = name.title()
        except:
            pass

    prompt = f"""
    Extract student informantion.
    Message:
    {last_msg}

    Rules:
    - If information is missing return null
    - Never return 'unknown'
    - Return only JSON

    Format:

    {{
        "name": null,
        "registration_no": null,
        "department": null
    }}
    """

    result = llm.invoke(prompt)
    
    try:
        raw = result.content.strip()

        start = raw.find("{")
        end = raw.rfind("}") + 1

        data = json.loads(raw[start:end])

        if data.get("name") and not state.get("student_name"):
            state["student_name"] = data["name"]
        if data.get("registration_no") and not state.get("registration_no"):
            state["registration_no"] = data["registration_no"]
        if data.get("department") and not state.get("department"):
            state["departement"] = data["department"]

    except:
        pass

    return state


