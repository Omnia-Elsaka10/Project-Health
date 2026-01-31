from pydantic import BaseModel
from typing import List
from app.schemas.task import TaskSchema

# This class defines the full structure of the data sent to the AI
class ProjectInput(BaseModel):
    project_name: str
    main_goals: str
    tasks: List[TaskSchema] # A list of the tasks defined in the other file