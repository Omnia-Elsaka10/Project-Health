import json
from app.core.llm import get_llm
from app.prompts.project_health import SYSTEM_PROMPT

def get_project_health_report(project_data: dict):
    # 1. Get the model
    llm = get_llm()
    
    # 2. Setup the prompt simply
    user_content = f"Project Data: {json.dumps(project_data)}"
    full_prompt = f"{SYSTEM_PROMPT}\n\n{user_content}"
    
    # 3. Call the model and get content directly
    response = llm.invoke(full_prompt)
    
    # 4. Clean and Parse (The magic part)
    content = response.content
    # Remove any markdown if the model tried to be smart
    clean_content = content.replace("```json", "").replace("```", "").strip()
    
    return json.loads(clean_content)