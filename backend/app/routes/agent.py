"""Agent Routes for Prompt Improvement"""
from fastapi import APIRouter, HTTPException
from app.models import PromptRequest, PromptResponse
from app.services import AgentService

router = APIRouter()
agent_service = AgentService()

@router.post("/improve", response_model=PromptResponse)
async def improve_prompt(request: PromptRequest) -> PromptResponse:
    """
    Improve a prompt using AI enhancement
    
    Args:
        request: PromptRequest with prompt and techniques
        
    Returns:
        PromptResponse with improved prompt
    """
    try:
        result = agent_service.improve_prompt(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "prompt-improver-api"}

@router.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Prompt Improver AI API",
        "version": "1.0.0",
        "endpoints": {
            "docs": "/docs",
            "improve": "/api/v1/prompts/improve"
        }
    }
