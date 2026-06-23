from typing import TypedDict, Optional, Annotated
from langgraph.graph.message import add_messages

class UniversityState(TypedDict):
    messages: Annotated[list, add_messages]

    student_name: Optional[str]
    registration_no: Optional[str]
    classification: Optional[str]

    query_category: str
    kb_context: str

    
