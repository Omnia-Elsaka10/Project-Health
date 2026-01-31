from pydantic import BaseModel
from typing import Optional

# This class defines what a "Task" looks like for the AI
class TaskSchema(BaseModel):
    title: str
    status: str  # Example: "Completed", "In Progress", "Overdue"
    assigned_to: str
    comments: Optional[str] = "No comments"