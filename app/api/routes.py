from fastapi import APIRouter, HTTPException
from app.services.health_service import get_project_health_report

router = APIRouter()

@router.post("/analyze-health")
async def analyze_health(data: dict):
    """
    API endpoint that receives project data and returns the AI health report.
    """
    try:
        # Call the service layer to process the data
        report = await get_project_health_report(data)
        return report
    except Exception as e:
        # Return a clear error if something goes wrong (e.g., API key issue)
        raise HTTPException(status_code=500, detail=str(e))