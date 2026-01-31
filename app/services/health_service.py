from app.core.llm import get_llm
from app.prompts.project_health import SYSTEM_PROMPT
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

async def get_project_health_report(project_data: dict):
    """
    Business logic to combine the prompt and data, then invoke the AI model.
    """
    model = get_llm()
    parser = JsonOutputParser()
    
    # Create the prompt structure
    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", "Analyze the following project data and goals: {data}")
    ])
    
    # Build the chain: Prompt -> LLM -> JSON Parser
    chain = prompt | model | parser
    
    # Run the chain with the actual project data
    report = chain.invoke({"data": project_data})
    return report