from utils.llm import llm
from graph.University_state import UniversityState

def classify_query(state):
    query = state["messages"][-1].content.lower()

    if "what is my name" in query:
        category = "memory"

    elif any(word in query for word in [
        "fee", "fees", "admission", "course",
        "eligibility", "application", "entrance",
        "b.tech", "m.tech"
    ]):
        category = "admission"

    elif any(word in query for word in [
        "hostel", "room", "mess", "wifi",
        "curfew", "facility"
    ]):
        category = "hostel"

    elif any(word in query for word in [
        "placement", "package", "salary", "company",
        "companies", "internship"
    ]):
        category = "placement"

    else:
        category = "academic"  # ← fallback prevents None crash

    return {"query_category": category}  # ← only return the changed key