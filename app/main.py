from fastapi import FastAPI
from app.api.routes import router

# Initialize the FastAPI application
app = FastAPI(
    title="Project Health AI Service",
    description="A microservice for analyzing project status using LLM reasoning."
)

# Register the AI routes with a prefix
app.include_router(router, prefix="/api/v1")

# Standard root endpoint
@app.get("/")
async def root():
    return {"status": "AI Service is Online"}