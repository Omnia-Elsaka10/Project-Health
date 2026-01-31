from fastapi import APIRouter, HTTPException
from app.services.health_service import get_project_health_report

router = APIRouter()

@router.post("/analyze-health")
async def analyze_health(data: dict):
    try:
        # We removed 'await' because the service function is now synchronous
        return get_project_health_report(data)
    except Exception as e:
        print(f"DEBUG ERROR: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))